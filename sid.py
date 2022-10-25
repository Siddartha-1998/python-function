import requests as req
import pandas as pd
import time
import pickle
import json
import csv
import openpyxl
# import schedule as shed
#About Global Demand in Crude Oil
import time
def run():
    l = []
    API_Key = 'EPvbpqLCa90jVF3r'

    # res = req.get('https://api.energyaspects.com/data/datasets/timeseries?api_key=%s' % API_Key)
    res = req.get('https://api.energyaspects.com/data/datasets/timeseries?api_key=%s' % API_Key)
    main = json.loads(res.text)

    for i in main:
        if "Monthly liquids demand" in i["metadata"]["description"]:
            l.append(i["dataset_id"])
        if "Monthly direct crude use/burn" in i["metadata"]["description"]:
            l.append(i["dataset_id"])
        if "Monthly total direct crude use/burn in kb/d" in i["metadata"]["description"]:
            l.append(i["dataset_id"])
    # print(l)
    _url = '&dataset_id='.join(map(str, l))
    inp_url = ['https://api.energyaspects.com/data/timeseries/json?api_key=EPvbpqLCa90jVF3r&date_from=2009-01-01&date_to=2023-01-01&dataset_id=']
    res_1 = inp_url[0] + _url
    res_2 = req.get(res_1)
    res_3 = res_2.text
    res_4 = json.loads(res_3)

    pd.DataFrame({i['metadata']['description']: i['data'] for i in res_4}).to_excel("Global_demand_Crude_oil.xlsx")
    wb = openpyxl.load_workbook('Global_demand_Crude_oil.xlsx')
    wb['Sheet1']['A1'] = 'Date'
    wb.save('Global_demand_Crude_oil.xlsx')
print(run())



# shed.every(1).seconds.do(run)


# while True:
#     shed.run_pending()
#     time.sleep(1)
    