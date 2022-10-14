import openpyxl
import requests as req
import csv
import json
from re import I
import pandas as pd
import os


class Global_middile_disslates():
    def run1():
        Start_id  = int(input("Enter Start Data Set_id:"))
        End_id = int(input("Enter End Data Set_id:"))
        
        for i in range(Start_id,End_id+1):#data set id 2296 - 2300
            request = ['https://api.energyaspects.com/data/timeseries/xlsx?dataset_id=']
            api_key =  'api_key=EPvbpqLCa90jVF3r'
    #&date_from=2009-01-01&date_to=2023-12-23``
            date_from = '2009-01-01'
            date_to = '2023-12-23'
            id = i
            res_1 = request[0] + str(i) + '&' + api_key + '&' + date_from  + '&' + date_to
            main = req.get(res_1)
    # r1 = json.loads(main.text)
            with open('sample_file_%s.xlsx' % str(i), mode='wb') as f:
                f.write(main.content)
            workbook1 = openpyxl.load_workbook('sample_file_%s.xlsx' % str(i))
            del workbook1['Metadata']
            extra = r'E:\\GE-PROJECT_DATABASE\\energy ascepts\\currently working on it\\test\\merge\MERGED_' + str(i) +  '.xlsx'
            workbook1.save(extra)
    
    
    
    # Merging all Excel data.
    
    
    
    #     BASE_DIR = 'E:\\GE-PROJECT_DATABASE\\energy ascepts\\currently working on it\\test\\merge'
    #     act_data = []; _columns = [] 

    #     for file in list(os.walk(BASE_DIR))[0][2]:
    #         df = pd.read_excel(BASE_DIR + '\\' + file)
    # # print(df.keys())
    #         if list(df.keys()):
    #           act_data.append(list(df[list(df.keys())[1]]))
    #           _columns.append(list(df.keys())[1])
    

    #     _index = list(df[list(df.keys())[0]]) 
    #     _index = _index if len(list(zip(*act_data))) == len(_index) else _index[:len(list(zip(*act_data)))]

    #     pd.DataFrame(list(zip(*([_index] + act_data))), columns=['Date'] + _columns
    #               ).to_excel(r'E:\GE-PROJECT_DATABASE\energy ascepts\currently working on it\test\Merged_xlsx\Global_Gasoline_Supply.xlsx',index=False,sheet_name = 'Global_gasoline_supply')
    # print(run1())
    