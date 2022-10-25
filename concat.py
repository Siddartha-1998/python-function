#Pandas is used as a dataframe to handle Excel files
from csv import excel
import pandas as pd
import os

# change the slash from “\” to “/”, if you are using Windows devices

input_file_path = "E:\\GE-PROJECT_DATABASE\\energy ascepts\\currently working on it\\all_crud_excel\\"
output_file_path = "E:\\GE-PROJECT_DATABASE\\energy ascepts\\currently working on it\\all_crud_excel\\"


excel_file_list = os.listdir(input_file_path)
# print(excel_file_list)



# print(df)


df = pd.DataFrame(excel_file_list)
print(df)

    
for excel_data in excel_file_list:
    df1 = pd.read_excel(input_file_path + excel_data)
    print(df1)
    if excel_data.endswith(".xlsx"):
        df_main = df.append(df1)
print(df_main.to_excel(output_file_path+"all_crude_test1.xlsx"))