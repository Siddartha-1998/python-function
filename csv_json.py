# import pandas as pd
# import json
# df = pd.read_csv(r'C:\Users\Techforce\Downloads\Testing the mario chat bot for time_lapse.csv')
# main = df.to_json (r'E:\GE_project\test2.json', indent=3)

# import pandas as pd
# import csv
# read_file = pd.read_excel (r'C:\Users\Techforce\OneDrive - Digitamize Inc\Testing the mario chat bot for time_lapse.xlsx')
# read_file.to_csv (r'E:\GE_project\csv.csv', index = None, header=True)


from distutils.log import ERROR
from typing import final
import pandas as pd
import json
from mysql.connector import connection

class data(object):
    def data():
        try:
            df = pd.read_excel(r'C:\Users\Techforce\OneDrive - Digitamize Inc\Testing the mario chat bot for time_lapse.xlsx')
            main = df.to_json (r'E:\GE_project\converted.json', indent=3)
            main_1 = df.to_csv (r'E:\GE_project\converted.csv',header=True)
            print(main,"json created")
            print(main_1,"csv created")
                
                
                
        except:
            print("ERROR")
        finally:
            ...
    print(data())
    


