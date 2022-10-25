import openpyxl
import requests as req
import csv
import json
from re import I
import pandas as pd
import os




class Global_middile_disslates():
    def run1():
        # Start_id  = int(input("Enter Start Data Set_id:"))
        # End_id = int(input("Enter End Data Set_id:"))
        
        for i in range(1,2+1):#data set id 2296 - 2300
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
            extra = r'E:\GE-PROJECT_DATABASE\Nikhil\test\Merged_MERGED_' + str(i) +  '.xlsx'
            workbook1.save(extra)
    print(run1())