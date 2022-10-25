from textwrap import indent
import requests as req
import pandas as pd
import time
import pickle
import json
import csv
import openpyxl


l = []
l1 = []
# ref = ['Angola', 'Congo', 'Algeria', 'Gabon', 'Equatorial_Guinea', 'Libya', 'Nigeria', 'Venezuela', 'UAE', 'Iraq', 'Iran', 'Kuwait', 'Saudi_Arabia', 'Burkina_Faso', 'Burundi', 'Benin', 'Botswana', 'Democratic_Republic_of_the_Congo', 'Central_African_Republic', 'Ivory_Coast', 'Cameroon', 'Cabo_Verde', 'Djibouti', 'Egypt', 'Western_Sahara', 'Eritrea', 'Ethiopia', 'Ghana', 'Gambia', 'Guinea', 'Guinea-Bissau', 'Kenya', 'Comoros', 'Liberia', 'Lesotho', 'Morocco', 'Madagascar', 'Mali', 'Mauritania', 'Mauritius', 'Malawi', 'Mozambique', 'Namibia', 'Niger', 'Rwanda', 'Seychelles', 'Sudan_and_South_Sudan', 'Saint_Helena', 'Sierra_Leone', 'Senegal', 'Somalia', 'Sao_Tome_and_Principe', 'Swaziland', 'Chad', 'Togo', 'Tunisia', 'Tanzania', 'Uganda', 'South_Africa', 'Zambia', 'Zimbabwe', 'American_Samoa', 'Australia', 'Bangladesh', 'Brunei', 'Bhutan', 'Cook_Islands', 'China', 'Fiji', 'Guam', 'Hong_Kong', 'Indonesia', 'India', 'Japan', 'Cambodia', 'Kiribati', 'North_Korea', 'South_Korea', 'Laos', 'Sri_Lanka', 'Myanmar', 'Mongolia', 'Macau', 'Maldives', 'Malaysia', 'New_Caledonia', 'Nepal', 'Nauru', 'Niue', 'New_Zealand', 'French_Polynesia', 'Papua_New_Guinea', 'Philippines', 'Pakistan', 'Solomon_Islands', 'Singapore', 'Thailand', 'Timor-Leste', 'East', 'Timor)', 'Tonga', 'Taiwan', 'US_Wake_Island', 'US_Hawaii', 'Vietnam', 'Vanuatu', 'Samoa', 'Albania', 'Austria', 'Bosnia_and_Herzegovina', 'Belgium', 'Bulgaria', 'Switzerland', 'Cyprus', 'Czechia', 'Germany', 'Denmark', 'Estonia', 'Spain', 'Finland', 'Faroe_Islands', 'France', 'United_Kingdom', 'Gibraltar', 'Greece', 'Croatia', 'Hungary', 'Ireland', 'Iceland', 'Italy', 'Lithuania', 'Luxembourg', 'Latvia', 'Montenegro', 'North_Macedonia', 'Malta', 'Netherlands', 'Norway', 'Poland', 'Portugal', 'Romania', 'Serbia', 'Sweden', 'Slovenia', 'Slovakia', 'Turkey', 'Afghanistan', 'Armenia', 'Azerbaijan', 'Belarus', 'Georgia', 'Kyrgyzstan', 'Kazakhstan', 'Moldova', 'Russia', 'Tajikistan', 'Turkmenistan', 'Ukraine', 'Uzbekistan', 'Antigua_and_Barbuda', 'Netherlands_Antilles', 'Argentina', 'Aruba', 'Barbados', 'Bolivia', 'Brazil', 'Bahamas', 'Belize', 'Chile', 'Colombia', 'Costa_Rica', 'Cuba', 'Dominica', 'Dominican_Republic', 'Ecuador', 'Falkland_Islands_(Malvinas)', 'Grenada', 'French_Guiana', 'Guadeloupe', 'Guatemala', 'Guyana', 'Honduras', 'Haiti', 'Jamaica', 'Saint_Kitts_and_Nevis', 'Cayman_Islands', 'Saint_Lucia', 'Martinique', 'Montserrat', 'Nicaragua', 'Panama', 'Peru', 'Puerto_Rico', 'Paraguay', 'Suriname', 'El_Salvador', 'Turks_and_Caicos_Islands', 'Trinidad_and_Tobago', 'Uruguay', 'Saint_Vincent_and_the_Grenadines', 'United_Kingdom_Virgin_Islands', 'US_Virgin_Islands', 'Bahrain', 'Israel', 'Jordan', 'Lebanon', 'Oman', 'Qatar', 'Syria', 'Yemen', 'Bermuda', 'Canada', 'Greenland', 'Mexico', 'Saint_Pierre_and_Miquelon', 'US_Alaska', 'US', 'Antarctica']
API_Key = 'EPvbpqLCa90jVF3r'

    # res = req.get('https://api.energyaspects.com/data/datasets/timeseries?api_key=%s' % API_Key)
res = req.get('https://api.energyaspects.com/data/datasets/timeseries?api_key=%s' % API_Key)
main = json.loads(res.text)
for i in main:
        if "OPEC crude production, EA forecast," in i["metadata"]["description"]:
            l.append(i["dataset_id"])
        if "Monthly OPEC " in i["metadata"]["description"]:
            l.append(i["dataset_id"])
        if "Total OPEC NGL production" in i["metadata"]["description"]:
            l.append(i["dataset_id"])
        if "Total OPEC Condensate production" in i["metadata"]["description"]:
            l.append(i["dataset_id"])
# print(l)
for j in l:
    # print(j)
    
    _url = '&dataset_id='.join(map(str, j))
    inp_url = ['https://api.energyaspects.com/data/timeseries/json?api_key=EPvbpqLCa90jVF3r&date_from=2009-01-01&date_to=2023-01-01&dataset_id=']
    res_1 = inp_url[0] + _url
    res_2 = req.get(res_1)
    res_3 = res_2.text
    res_4 = json.loads(res_3)
    # with open("OPEC.json",'w') as f:
    #     res_5 = json.dump(res_4,f,indent = 4)
    for k in res_4:
        print(k["metadata"]["description"])
        
        

    # pd.DataFrame({k['metadata']['description']: k['data'] for k in res_4}).to_excel("OPEC_oil.xlsx")
    # wb = openpyxl.load_workbook('OPEC_oil.xlsx')
    # wb['Sheet1']['A1'] = 'Date'
    # wb.save('OPEC_oil.xlsx')


# .DataFrame({i['metadata']['description']: i['data'] for i in res_4}).to_excel("Global_demand_Crude_oil.xlsx")
#     wb = openpyxl.load_workbook('Global_demand_Crude_oil.xlsx')
#     wb['Sheet1']['A1'] = 'Date'
#     wb.save('Global_demand_Crude_oil.xlsx')
    

    







































































    
    

    