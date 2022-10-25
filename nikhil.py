import pandas as pd
import requests
import os
import sys
import json
from collections import OrderedDict
import pickle
from glob import glob
from flask import (Flask, 
                   request, 
                   jsonify)
import requests
from flask_apscheduler import APScheduler
from mysql.connector import connection
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import encoders
import ssl
import smtplib
from pprint import pprint
import logging


# logging.basicConfig(level=logging.DEBUG,
                    # datefmt='%H:%M:%S',
                    # format='[%(process)s] ---> %(asctime)10s %(msecs)10s %(message)10s')
# logger = logging.getLogger(__name__)
    
 
with open(glob('C:\\Us**\\91**\\Docu**\\mys**cre****_new.pickle')[0], mode='rb') as f:
    creds = pickle.load(f)
  
with open(glob('C:\\Us**\\91**\\greatshippi***_pro******de***.json')[0], mode='r') as f1:
    mail_details = json.load(f1)

class Config:
    SCHEDULER_API_ENABLED = True

app = Flask(__name__)
app.config.from_object(Config())

scheduler = APScheduler()
scheduler.init_app(app)
scheduler.start()

def send_mail(file_path, sub_category):
    print('==== Thread went to send mails =======')
    _body = '<!doctype html>\n<html>\n<body>\n' + \
            '<p>Please find the report for %s </p>' + \
            '<p>warm regards, <br> Nikhil Manvesh, <br> (Junior Product Engineer)</p>' + \
            '</body>\n</html>'
    _body = _body % sub_category
            
    # with open('img/tfai_image.png', mode='rb') as f:
        # logo_msg = MIMEImage(f.read())
    # logo_msg.add_header('Content-ID', '<logo>')
    with open(file_path, mode='rb') as f:
        pay_load_obj = MIMEBase('application', 'octet-stream')
        pay_load_obj.set_payload(f.read())
        encoders.encode_base64(pay_load_obj)
        pay_load_obj.add_header('Content-Disposition', 'attachment; filename= %s' % os.path.basename(file_path))
    
    msg = MIMEMultipart()
    msg['subject'] = 'Report for %s' % sub_category
    msg['from'] = mail_details['GS_Mail_From']
    msg['to'] = ','.join(mail_details['GS_Mail_To'])
    msg['cc'] = ','.join(mail_details['GS_Mail_CC'])
    msg['bcc'] = ','.join(mail_details['GS_Mail_BCC'])
    msg.attach(MIMEText(_body, 'html'))
    # msg.attach(logo_msg)
    msg.attach(pay_load_obj)
    # new_msg = msg.as_string()
    
    _context = ssl.create_default_context()
    
    with smtplib.SMTP(mail_details['Host'], mail_details['Port']) as smtp:
        smtp.starttls(context=_context)
        try:
            smtp.login(mail_details['GS_Mail_From'], mail_details['GS_Mail_Password'])
            smtp.send_message(msg)
        except Exception as ex:
            print((type(ex), sys.exc_info()[1], sys.exc_info()[2]))
        else:
            print('Mail sent succesfully')
        


def merge_monthly_demand_data(sub_category, API_Key, from_date, to_date):

    with open('Input_Files\\countries_order.json', mode='r') as f:
        order_list = json.load(f)['order']
        
    res_dict = {}
    
    res = requests.get(url='https://api.energyaspects.com/data/datasets/timeseries?api_key=%s' % API_Key)
    _ids = [i['dataset_id'] for i in res.json() if sub_category in i['metadata']['description']]
    print(_ids)
    _url = ('https://api.energyaspects.com/data/timeseries/json?api_key=%s&date_from=%s&date_to=%s' % (API_Key, from_date, to_date)) + \
            '&data_set_id=' + '&dataset_id='.join(map(str, _ids))
    _res_dict = {i['metadata']['description']: i['data'] for i in requests.get(url=_url).json()}
    res_list = []
    for country in order_list:
        try:
            res_list.append(['Monthly ' + '%s for %s in kb/d' % (sub_category, country), list(_res_dict.get('Monthly ' + '%s for %s in kb/d' % (sub_category, country)).values())]) 
        except Exception as ex:
            try:
                res_list.append(['Monthly ' + '%s for %s in kbbl_d' % (sub_category, country), list(_res_dict.get('Monthly ' + '%s for %s in kbbl_d' % (sub_category, country)).values())])
            except Exception as ex:
                diff_data = [res_list.append([rec, list(_res_dict[rec].values())]) for rec in list(_res_dict.keys()) if country in rec]

    try:
        os.mkdir('Output_Files')
    except Exception as ex:
        print((type(ex), sys.exc_info()[1], sys.exc_info()[2]))
        
    merged_excel_path = 'Output_files' + '\\' + sub_category.replace(' ', '_') + '.xlsx'
    max_value = max(res_list, key=lambda x: len(x[1]))
    final_res_list = [[i[0], i[1] + ([''] * (len(max_value[1]) - len(i[1])))] if len(i[1]) < len(max_value[1]) else i for i in res_list]
    pd.DataFrame(OrderedDict(final_res_list), index=list(_res_dict.get(max_value[0]).keys())).to_excel(merged_excel_path)

    send_mail(merged_excel_path, sub_category)
    
# merge_monthly_demand_data('Monthly jet demand', 'uOh6O6TGvp91qSfT', '2009-01-01', '2023-12-23')

@app.route('/update/data/', methods=['POST'])
def update_date():
    conn = connection.MySQLConnection(user=creds['user_name'], password=creds['password'], host='localhost', database='GreatShipping_DB')
    cursor = conn.cursor()
    cursor.execute('TRUNCATE TABLE global_variables')
    cursor.execute('INSERT INTO global_variables (API_Key, from_date, to_date, minute, hour, day_of_week, category, sub_category, job_id, job_type) values ' + \
                    str((request.json['API_Key'], request.json['from_date'], 
                         request.json['to_date'], request.json['minute'], 
                         request.json['hour'], request.json['day_of_week'], 
                         request.json['category'], request.json['sub_category'],
                         request.json['job_id'], request.json['job_type'])))
    conn.commit()
    cursor.execute('SELECT * FROM global_variables')
    _data = list(cursor)[0]
    cursor.close()
    conn.close()
    
    @scheduler.task(_data[-1], id=_data[-2], minute=_data[3], hour=_data[4], day_of_week=_data[5])
    def fetch_and_merge_exceldata():
        merge_monthly_demand_data(_data[-3], _data[0], _data[1], _data[2])
        logging.basicConfig(level=logging.INFO, datefmt='%H:%M:%S', format='[%(process)s] ---> %(asctime)10s %(msecs)10s %(message)10s')
    
    return jsonify({'message': 'data updated successfully'})
    

if __name__ == '__main__':
    app.run(debug=True)