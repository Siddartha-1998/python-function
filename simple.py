import json
import csv
import pandas as pd
import requests as req
import os
import openpyxl
#'https://api.energyaspects.com/data/timeseries/?api_key=EPvbpqLCa90jVF3r&date_from=2009-01-01&date_to=2023-12-23&dataset_id=2069' 

l = [] 
s = []
l1 = []
_dict = {}
res_data = []
# # # Global disel Demand.
for i in range(1933,2070+1):#intailizing data Set From to End Range.
    # Getting data from API.
    request = ['https://api.energyaspects.com/data/timeseries/json?api_key=EPvbpqLCa90jVF3r&date_from=2009-01-01&date_to=2023-12-23&dataset_id=']
    id = i
    res_1 = request[0]+str(i)
    main = req.get(res_1) #Get method to get the Data fro  API
    r1 = json.loads(main.text)#converting the API Data into JSON
    resp = r1[0]  #Data is in list
    data = str(resp['metadata']['description'].replace('kbbl_d','kb/d') + str(resp['data']))#From that data we need fetch the description and date.(data) is key for date.
    l.append(data)



# # # # # #converting the json data into a mulitiple list of Dictionarys.


for j in range(0,len(l)):
    _dict['description'] = l[j][: l[j].find('kb/d') + 4]#Slicing the uneccasary data from descripition and we need only kb/d part
    _dict['date'] = eval(l[j][l[j].find('kb/d') + 4: ])#in date we need only Date Constraint and Values. we didn't need  kb/d part We Removing that.
    res_data.append(_dict)
    _dict = {} 

# # #     #Total Api of json data is converting into a dictionary 


# # # #That dictonary data(res_data) is Dumping into the Single JSON data.
DIR_1 = ['E:\\GE-PROJECT_DATABASE\\energy ascepts\\currently working on it\\test\\BLOCK\\Global_disel_demand_main_1.json']
with open(DIR_1[0],'w') as f:
    json.dump(res_data, f,indent = 4)
    
# # We are loading that dumped data into another res_2 Variable.

with open(DIR_1[0],'r') as f:
    res_2 = json.load(f)
pd.DataFrame(res_2)

# # Converting data  according into country sequence sheet What client given.
for k in res_2:
    m1 = k["description"]
    s1 = []
    s1.append(m1)
    for l in range(len(s1)):
        m2 = s1[l]
        # name = 'diesel'
        if  m2 in k["description"]:
            main_1 = m2.replace('kb/d',"kb_d")
            # print(main_1)
            Base_Dir_1 = ['E:\\GE-PROJECT_DATABASE\\energy ascepts\\currently working on it\\test\\merge\\']
            # dir = Base_Dir_1[0] + '%s'+ "\\" + str(m2)
            print(pd.DataFrame([k["description"]] + list(k.get("date").values()),["Date"] +list(k.get("date").keys())).to_excel(Base_Dir_1[0]+ str(main_1) + '.xlsx',index = True))











ref = ['Angola',
'Ivory Coast',
'Congo',
'Cameroon',
'Algeria',
'Egypt',
'Gabon',
'Ghana',
'Kenya',
'Libya',
'Morocco',
'Nigeria',
'Sudan',
'Senegal',
'Tunisia',
'Tanzania',
'Zambia',
'Australia',
'Bangladesh',
'South Africa',
'Brunei Darussalam',
'China',
'Hong Kong',
'Indonesia',
'India',
'Japan',
'Korea',
'Sri Lanka',
'Myanmar',
'Malaysia',
'New Zealand',
'Papua New Guinea',
'Philippines',
'Pakistan',
'Singapore',
'Thailand',
'Taiwan',
'Vietnam',
'Austria',
'Bosnia and Herzegovnia',
'Belgium',
'Bulgaria',
'Switzerland',
'Cyprus',
'Czechia',
'Germany',
'Denmark',
'Estonia',
'Spain',
'Finland',
'France',
'United Kingdom',
'Greece',
'Croatia',
'Hungary',
'Ireland',
'Iceland',
'Italy',
'Lithuania',
'Luxembourg',
'Latvia',
'Montenegro',
'Macedonia',
'Malta',
'Netherlands',
'Norway',
'Poland',
'Portugal',
'Romania',
'Serbia',
'Sweden',
'Slovenia',
'Slovakia',
'Turkey',
'Azerbaijan',
'Belarus',
'Georgia',
'Kazakhstan',
'Moldova',
'Russia',
'Turkmenistan',
'Ukraine',
'Uzbekistan',
'Argentina',
'Bolivia',
'Brazil',
'Chile',
'Colombia',
'Costa Rica',
'Cuba',
'Curacao',
'Dominican Republic',
'Ecuador',
'Guatemala',
'Honduras',
'Jamaica',
'Mexico',
'Nicaragua',
'Panama',
'Peru',
'Puerto Rico',
'El Salvador',
'Trinidad and Tobago',
'Uruguay',
'Venezuela',
'US Virgin Islands',
'United Arab Emirates',
'Bahrain',
'Israel',
'Iraq',
'Iran',
'Jordan',
'Kuwait',
'Oman',
'Qatar',
'Saudi Arabia',
'Syria',
'Yemen',
'Canada',
'US PADD1',
'US PADD2',
'US PADD3',
'US PADD4',
'US PADD5'
]


#E:\\GE-PROJECT_DATABASE\\energy ascepts\\currently working on it\\test\\merge\\Monthly diesel demand for'

BASE_DIR = 'E:\\GE-PROJECT_DATABASE\\energy ascepts\\currently working on it\\test\\merge\\Monthly diesel demand for'
act_data = []; _columns = [] 

for i in ref:
    df = pd.read_excel(BASE_DIR + " " + i + " " + "in kb_d"  + '.xlsx')
    if list(df.keys()):
        act_data.append(list(df[list(df.keys())[1]]))
        _columns.append(list(df[list(df.keys())[1]])[0])

date_column = list(df[df.keys()[0]])


pd.DataFrame(list(zip(*([date_column] + act_data)))
            ).to_excel(r'E:\GE-PROJECT_DATABASE\energy ascepts\currently working on it\test\Merged_xlsx\Global_disel_demand.xlsx',index=False,sheet_name = 'test',header = True)
print("DATA IS MERGED INTO SINGLE EXCEL FILE.")


filename = r"E:\GE-PROJECT_DATABASE\energy ascepts\currently working on it\test\Merged_xlsx\Global_disel_demand.xlsx"
wb = openpyxl.load_workbook(filename)
sheet = wb['test']

sheet.delete_rows(1, 1)
wb.save(filename)






































