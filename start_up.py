import pandas as pd
import requests
import os
import sys
import json
from collections import OrderedDict
import pickle
from glob import glob
from flask import Flask
from flask_apscheduler import APScheduler



class Config:
    SCHEDULER_API_ENABLED = True

app = Flask(__name__)
app.config.from_object(Config())

scheduler = APScheduler()
scheduler.init_app(app)
scheduler.start()

@scheduler.task('cron', id='job_five', minute='31', hour='00', day_of_week='tue')
def fetch_and_merge_exceldata():
    with open(glob('C:\\Us**\\91**\\Docu**\\Gr**S**di**API**.pickle')[0], mode='rb') as f:
        _key = pickle.load(f)
        
    with open('Input_Files\\countries_order.json', mode='r') as f:
        order_list = json.load(f)['order']
        
    res_dict = {}
    for dataset_id in range(1933, 2070+1):
        _url = 'https://api.energyaspects.com/data/timeseries/json?api_key=%s&date_from=2009-01-01&date_to=2023-12-23&dataset_id=%s' % (_key['_key'], str(dataset_id))
        main = requests.get(url=_url)
        res_dict[main.json()[0].get('metadata')['description'].\
                 replace('Monthly diesel demand for ', '').\
                 replace(' in kb/d', '').replace(' in kbbl_d', '')] = [main.json()[0].get('metadata')['description'], main.json()[0].get('data')]

    try:
        os.mkdir('Output_Files')
    except Exception as ex:
        print(type(ex), sys.exc_info()[1], sys.exc_info()[2])
    pd.DataFrame(OrderedDict([[res_dict[country][0], res_dict[country][1]] for country in order_list])).to_excel('Output_Files/diesel_demand_for_all_countries.xlsx')
    
    
    
if __name__ == '__main__':
    app.run()
