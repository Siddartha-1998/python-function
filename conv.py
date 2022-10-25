import csv
import json
from re import I
import pandas as pd
import os



BASE_DIR = 'E:\\GE-PROJECT_DATABASE\\energy ascepts\\currently working on it\\Oil products\\Global disel demand'
act_data = []; _columns = [] 

for file in list(os.walk(BASE_DIR))[0][2]:
    df = pd.read_excel(BASE_DIR + '\\' + file)
    # print(df.keys())
    if list(df.keys()):
        act_data.append(list(df[list(df.keys())[1]]))
        _columns.append(list(df.keys())[1])
    

_index = list(df[list(df.keys())[0]])
_index = _index if len(list(zip(*act_data))) == len(_index) else _index[:len(list(zip(*act_data)))]

pd.DataFrame(list(zip(*([_index] + act_data))), columns=['Date'] + _columns
             ).to_excel('Global_Disel_Demand_excels.xlsx',
                        index=False)
