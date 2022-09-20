import pandas as pd
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import ssl
import smtplib
import sys
import os
from bs4 import BeautifulSoup
import pickle

# Create your views here.

def send_mail(file_path, _from='npeyyala@techforce.ai', to_emails=[], subject='Test || Mail', 
              html_body='This is just a sample test mail. Please ignore', body_type='plain', *args, **kwargs):

    data_frame = pd.read_excel(file_path)
    data_frame_one = list(zip(*[list(data_frame[i]) for i in data_frame.keys()]))
    _data_frame_one = [[j if str(j) != 'nan' else '' for j in i] for i in data_frame_one]
    data_frame_two = pd.DataFrame(_data_frame_one[1:], columns=_data_frame_one[0])
    # print(data_frame_two)
    df_html = data_frame_two.to_html(index=False)
    # print(df_html)

    with open('C:\\RPA Flows\\Downloded Reports\\TFAIPythonScripts\\TechForce-Logo.png', mode='rb') as f:
        logo_msg = MIMEImage(f.read())
    # print(logo_msg)
    logo_msg.add_header('Content-ID', '<logo>')

    with open(file_path, mode='rb') as f1:
        attachment = MIMEBase('application', 'octet-stream')
        attachment.set_payload(f1.read())
        encoders.encode_base64(attachment)
    attachment.add_header('Content-Disposition', "attachment; filename=%s" % os.path.basename(file_path))
    
    html_body = """\
        <!doctype html>
        <html>
            <body>
                Hi All,<br>
                Please check the following report<br><br>
                %s<br><br>warm regards,<br>Nikhil Manvesh Peyyala.<br><img src="cid:logo" alt="" width=130 height=40>
            </body>
        </html>
        """ % df_html
    
    with open('ol_password.pickle', mode='rb') as f1:
        _password = pickle.load(f1)['password']

    msg = MIMEMultipart()
    msg['subject'] = subject
    msg['from'] = _from
    msg['to'] = ','.join(to_emails)
    msg.attach(MIMEText(html_body, body_type))
    msg.attach(attachment)
    msg.attach(logo_msg)
    
    _context = ssl.create_default_context()
    
    with smtplib.SMTP('smtp.office365.com', 587) as smtp:
        smtp.starttls(context=_context)
        smtp.login(_from, _password)
        smtp.send_message(msg)


send_mail(file_path='C:\\RPA Flows\\Downloded Reports\\braeamar_files\\FFA Report 19-09-2022.xlsx',
         to_emails=['npeyyala@techforce.ai', 'sgarigipati@techforce.ai', 'Skayithi@techforce.ai'], body_type='Html')
            
