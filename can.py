import csv
import json
from re import I
import pandas as pd
import os


BASE_DIR = 'E:\\GE-PROJECT_DATABASE\energy ascepts\\currently working on it'
_files = list(os.walk(BASE_DIR + '\\' + 'crud oil data\\test'))[0][2]
l = []
# for i in _files:
#     df = pd.read_excel(r'E:\GE-PROJECT_DATABASE\energy ascepts\currently working on it\crud oil data\test\\' + i)
#     print(df)
  
#     res_list = []
#     date_col = []
#     res_list.append([df.keys()[1]] + list(df[df.keys()[1]]))
#     date_col.append(['Date'] + list(df['Date']))
#     pd.DataFrame(list(zip(*(date_col + res_list)))[1:], columns=list(zip(*(date_col + res_list)))[0]).to_excel('saibaba.xlsx', index=False,sheet_name = 'Test')        
                    
                
 
            
        
        
for i in range(0,len(_files)):
    main = _files[i]
   
    df = pd.read_excel(r'E:\GE-PROJECT_DATABASE\energy ascepts\currently working on it\crud oil data\test\\' + main)
    print(df)
   
    res_list = []
    date_col = []
    for ind, file in enumerate(main):
        df = pd.read_excel(file)
        res_list.append([df.keys()[1]] + list(df[df.keys()[1]]))
        if not ind:
            date_col.append(['Date'] + list(df['Date']))
            pd.DataFrame(list(zip(*(date_col + res_list)))[1:], columns=list(zip(*(date_col + res_list)))[0]).to_excel('test.xlsx', index=False,sheet_name = 'test')        
                
                
 