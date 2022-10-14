import json
import pandas as pd
import requests as req
import os
# r1 = req.get('https://api.energyaspects.com/data/timeseries/?api_key=EPvbpqLCa90jVF3r&date_from=2009-01-01&date_to=2023-12-23&dataset_id=2069')
# print(eval(r1.text))
l = [] 
l1 = []
_dict = {}
res_data = []
#Gloabl disel Demand.
for i in range(1964,2070+1):#intailizing data Set From to End Range.
    #Getting data from API.
    request = ['https://api.energyaspects.com/data/timeseries/json?api_key=EPvbpqLCa90jVF3r&date_from=2009-01-01&date_to=2023-12-23&dataset_id=']
    id = i
    res_1 = request[0]+str(i)
    main = req.get(res_1) #Get method to get the Data fro  API
    r1 = json.loads(main.text)#converting the API Data into JSON
    resp = r1[0]  #Data is in list
    data = str(resp['metadata']['description'].replace('kbbl_d','kb/d') + str(resp['data']))#From that data we need fetch the description and date.(data) is key for date.
    l.append(data)
l
# print(l)

#converting the json data into a mulitiple list of Dictionarys.


for j in range(0,len(l)):
    _dict['description'] = l[j][: l[j].find('kb/d') + 4] #Slicing the uneccasary data from descripition and we need only kb/d part
    _dict['date'] = eval(l[j][l[j].find('kb/d') + 4: ])#in date we need only Date Constraint and Values. we didn't need  kb/d part We Removing that.
    res_data.append(_dict)
    _dict = {} 
    # kbbl_d 1971
    #Total Api of json data is converting into a dictionary 


#That dictonary data(res_data) is Dumping into the Single JSON data.
with open('E:\\GE-PROJECT_DATABASE\\energy ascepts\\currently working on it\\test\\BLOCK\\test_main.json','w') as f:
    json.dump(res_data, f,indent = 4)
    
# We are loading that dumped data into another res_2 Variable.
with open('E:\\GE-PROJECT_DATABASE\\energy ascepts\\currently working on it\\test\\BLOCK\\test_main.json','r') as f:
    res_2 = json.load(f)
pd.DataFrame(res_2)
c = 0
# Converting data  according into country sequence sheet What client given.
for k in res_2:
    name = 'diesel' 
    if 'Monthly'+ " " + str(name) + " " +'demand for Angola in kb/d' in k["description"]:
        print(pd.DataFrame([k["description"]] + list(k.get("date").values()),["Date"] +list(k.get("date").keys())).to_excel(r"E:\GE-PROJECT_DATABASE\energy ascepts\currently working on it\test\merge\Angola.xlsx",index = True))
      

        print("-----------------------------------------------------------")
    if 'Monthly'+ " " + str(name) + " " +'demand for Ivory Coast in kb/d' in k["description"] :
        print(pd.DataFrame([k["description"]] + list(k.get("date").values()),["Date"] +list(k.get("date").keys())).to_excel(r"E:\GE-PROJECT_DATABASE\energy ascepts\currently working on it\test\merge\Ivory_Coast.xlsx",index = True))
        print("-----------------------------------------------------------")
    
    if 'Monthly'+ " " + str(name) + " " +'demand for Congo in kb/d' in  k["description"] :
        print(pd.DataFrame([k["description"]] + list(k.get("date").values()),["Date"] +list(k.get("date").keys())).to_excel(r"E:\GE-PROJECT_DATABASE\energy ascepts\currently working on it\test\merge\Congo.xlsx",index = True))
      
        
        print("-----------------------------------------------------------")
        
    if 'Monthly'+ " " + str(name) + " " + 'demand for Cameroon in kb/d' in k["description"]:
        print(pd.DataFrame([k["description"]] + list(k.get("date").values()),["Date"] +list(k.get("date").keys())).to_excel(r"E:\GE-PROJECT_DATABASE\energy ascepts\currently working on it\test\merge\Cameroon.xlsx",index = True))
      
        print("-----------------------------------------------------------")
        
    if 'Monthly'+ " " + str(name) + " " + 'demand for Algeria in kb/d' in k["description"] :
        print(pd.DataFrame([k["description"]] + list(k.get("date").values()),["Date"] +list(k.get("date").keys())).to_excel(r"E:\GE-PROJECT_DATABASE\energy ascepts\currently working on it\test\merge\Algeria.xlsx",index = True))
      
        print("-----------------------------------------------------------")
        
    if  'Monthly'+ " " + str(name) + " " + 'demand for Egypt in kb/d' in k["description"]:
        print(pd.DataFrame([k["description"]] + list(k.get("date").values()),["Date"] +list(k.get("date").keys())).to_excel(r"E:\GE-PROJECT_DATABASE\energy ascepts\currently working on it\test\merge\Egypt.xlsx",index = True))
      
        print("-----------------------------------------------------------")
        
    if  'Monthly'+ " " + str(name) + " " + 'demand for Gabon in kb/d' in k["description"]:
        print(pd.DataFrame([k["description"]] + list(k.get("date").values()),["Date"] +list(k.get("date").keys())).to_excel(r"E:\GE-PROJECT_DATABASE\energy ascepts\currently working on it\test\merge\Gabon.xlsx",index = True))
      
        print("-----------------------------------------------------------")
    if  'Monthly'+ " " + str(name) + " " + 'demand for Ghana in kb/d' in k["description"]:
        print(pd.DataFrame([k["description"]] + list(k.get("date").values()),["Date"] +list(k.get("date").keys())).to_excel(r"E:\GE-PROJECT_DATABASE\energy ascepts\currently working on it\test\merge\Ghana.xlsx",index = True))
      
        print("-----------------------------------------------------------")
    if  'Monthly'+ " " + str(name) + " " + 'demand for Kenya in kb/d' in k["description"]:
        print(pd.DataFrame([k["description"]] + list(k.get("date").values()),["Date"] +list(k.get("date").keys())).to_excel(r"E:\GE-PROJECT_DATABASE\energy ascepts\currently working on it\test\merge\Kenya.xlsx",index = True))
      
        print("-----------------------------------------------------------")
    if  'Monthly'+ " " + str(name) + " " + 'demand for Libya in kb/d' in k["description"]:
        print(pd.DataFrame([k["description"]] + list(k.get("date").values()),["Date"] +list(k.get("date").keys())).to_excel(r"E:\GE-PROJECT_DATABASE\energy ascepts\currently working on it\test\merge\Libya.xlsx",index = True))
      
        print("-----------------------------------------------------------")
    if  'Monthly'+ " " + str(name) + " " + 'demand for Morocco in kb/d' in k["description"]:
        print(pd.DataFrame([k["description"]] + list(k.get("date").values()),["Date"] +list(k.get("date").keys())).to_excel(r"E:\GE-PROJECT_DATABASE\energy ascepts\currently working on it\test\merge\Morocco.xlsx",index = True))
      
        print("-----------------------------------------------------------")

      
        print("-----------------------------------------------------------")
    if  'Monthly'+ " " + str(name) + " " + 'demand for Nigeria in kb/d' in k["description"]:
        print(pd.DataFrame([k["description"]] + list(k.get("date").values()),["Date"] +list(k.get("date").keys())).to_excel(r"E:\GE-PROJECT_DATABASE\energy ascepts\currently working on it\test\merge\Nigeria.xlsx",index = True))
      
        print("-----------------------------------------------------------")
    if  'Monthly'+ " " + str(name) + " " + 'demand for Sudan in kb/d' in k["description"]:
        print(pd.DataFrame([k["description"]] + list(k.get("date").values()),["Date"] +list(k.get("date").keys())).to_excel(r"E:\GE-PROJECT_DATABASE\energy ascepts\currently working on it\test\merge\Sudan.xlsx",index = True))
      
        print("-----------------------------------------------------------")
    if  'Monthly'+ " " + str(name) + " " + 'demand for Senegal in kb/d' in k["description"]:
        print(pd.DataFrame([k["description"]] + list(k.get("date").values()),["Date"] +list(k.get("date").keys())).to_excel(r"E:\GE-PROJECT_DATABASE\energy ascepts\currently working on it\test\merge\Senegal.xlsx",index = True))
      
        print("-----------------------------------------------------------")
    if  'Monthly'+ " " + str(name) + " " + 'demand for Tunisia in kb/d' in k["description"]:
        print(pd.DataFrame([k["description"]] + list(k.get("date").values()),["Date"] +list(k.get("date").keys())).to_excel(r"E:\GE-PROJECT_DATABASE\energy ascepts\currently working on it\test\merge\Tunisia.xlsx",index = True))
      
        print("-----------------------------------------------------------")
    if  'Monthly'+ " " + str(name) + " " + 'demand for Tanzania in kb/d' in k["description"]:
        print(pd.DataFrame([k["description"]] + list(k.get("date").values()),["Date"] +list(k.get("date").keys())).to_excel(r"E:\GE-PROJECT_DATABASE\energy ascepts\currently working on it\test\merge\Tanzania.xlsx",index = True))
      
        print("-----------------------------------------------------------")
    if  'Monthly'+ " " + str(name) + " " + 'demand for South Africa in kb/d' in k["description"]:
        print(pd.DataFrame([k["description"]] + list(k.get("date").values()),["Date"] +list(k.get("date").keys())).to_excel(r"E:\GE-PROJECT_DATABASE\energy ascepts\currently working on it\test\merge\South Africa.xlsx",index = True))
      
        print("-----------------------------------------------------------")
    if  'Monthly'+ " " + str(name) + " " + 'demand for Zambia in kb/d' in k["description"]:
        print(pd.DataFrame([k["description"]] + list(k.get("date").values()),["Date"] +list(k.get("date").keys())).to_excel(r"E:\GE-PROJECT_DATABASE\energy ascepts\currently working on it\test\merge\Zambia.xlsx",index = True))
      
        print("-----------------------------------------------------------")
    if  'Monthly'+ " " + str(name) + " " + 'demand for Australia in kb/d' in k["description"]:
        print(pd.DataFrame([k["description"]] + list(k.get("date").values()),["Date"] +list(k.get("date").keys())).to_excel(r"E:\GE-PROJECT_DATABASE\energy ascepts\currently working on it\test\merge\Australia.xlsx",index = True))
      
        print("-----------------------------------------------------------")
    if  'Monthly'+ " " + str(name) + " " + 'demand for  in kb/d' in k["description"]:
        print(pd.DataFrame([k["description"]] + list(k.get("date").values()),["Date"] +list(k.get("date").keys())).to_excel(r"E:\GE-PROJECT_DATABASE\energy ascepts\currently working on it\test\merge\Bangladesh.xlsx",index = True))

        print("-----------------------------------------------")
        
    if  'Monthly'+ " " + str(name) + " " + 'demand for Brunei in kb/d' in k["description"]:
        print(pd.DataFrame([k["description"]] + list(k.get("date").values()),["Date"] +list(k.get("date").keys())).to_excel(r"E:\GE-PROJECT_DATABASE\energy ascepts\currently working on it\test\merge\Brunei.xlsx",index = True))

        print("-----------------------------------------------")
    if  'Monthly'+ " " + str(name) + " " + 'demand for China in kb/d' in k["description"]:
        print(pd.DataFrame([k["description"]] + list(k.get("date").values()),["Date"] +list(k.get("date").keys())).to_excel(r"E:\GE-PROJECT_DATABASE\energy ascepts\currently working on it\test\merge\China.xlsx",index = True))
    
        print("-----------------------------------------------") 
    if  'Monthly'+ " " + str(name) + " " + 'demand for Hong Kong in kb/d' in k["description"]:
        print(pd.DataFrame([k["description"]] + list(k.get("date").values()),["Date"] +list(k.get("date").keys())).to_excel(r"E:\GE-PROJECT_DATABASE\energy ascepts\currently working on it\test\merge\Hong Kong.xlsx",index = True))
    
        print("-----------------------------------------------")  
    if  'Monthly'+ " " + str(name) + " " + 'demand for Indonesia in kb/d' in k["description"]:
        print(pd.DataFrame([k["description"]] + list(k.get("date").values()),["Date"] +list(k.get("date").keys())).to_excel(r"E:\GE-PROJECT_DATABASE\energy ascepts\currently working on it\test\merge\Indonesia.xlsx",index = True))
        c += 1
        print("-----------------------------------------------")
    if  'Monthly'+ " " + str(name) + " " + 'demand for India in kb/d' in k["description"]:
        print(pd.DataFrame([k["description"]] + list(k.get("date").values()),["Date"] +list(k.get("date").keys())).to_excel(r"E:\GE-PROJECT_DATABASE\energy ascepts\currently working on it\test\merge\India.xlsx",index = True))
        c += 1
        print("-----------------------------------------------")
    if  'Monthly'+ " " + str(name) + " " + 'demand for Japan in kb/d' in k["description"]:
        print(pd.DataFrame([k["description"]] + list(k.get("date").values()),["Date"] +list(k.get("date").keys())).to_excel(r"E:\GE-PROJECT_DATABASE\energy ascepts\currently working on it\test\merge\Japan.xlsx",index = True))
        c += 1
        print("-----------------------------------------------")
    if  'Monthly'+ " " + str(name) + " " + 'demand for Korea in kb/d' in k["description"]:
        print(pd.DataFrame([k["description"]] + list(k.get("date").values()),["Date"] +list(k.get("date").keys())).to_excel(r"E:\GE-PROJECT_DATABASE\energy ascepts\currently working on it\test\merge\Korea.xlsx",index = True))
        c += 1
        print("-----------------------------------------------")
    if  'Monthly'+ " " + str(name) + " " + 'demand for Sri Lanka in kb/d' in k["description"]:
        print(pd.DataFrame([k["description"]] + list(k.get("date").values()),["Date"] +list(k.get("date").keys())).to_excel(r"E:\GE-PROJECT_DATABASE\energy ascepts\currently working on it\test\merge\Sri Lanka.xlsx",index = True))
        c += 1
        print("-----------------------------------------------") 
    if  'Monthly'+ " " + str(name) + " " + 'demand for Myanmar in kb/d' in k["description"]:
        print(pd.DataFrame([k["description"]] + list(k.get("date").values()),["Date"] +list(k.get("date").keys())).to_excel(r"E:\GE-PROJECT_DATABASE\energy ascepts\currently working on it\test\merge\Myanmar.xlsx",index = True))
        c += 1
        print("-----------------------------------------------")
    if  'Monthly'+ " " + str(name) + " " + 'demand for Malaysia in kb/d' in k["description"]:
        print(pd.DataFrame([k["description"]] + list(k.get("date").values()),["Date"] +list(k.get("date").keys())).to_excel(r"E:\GE-PROJECT_DATABASE\energy ascepts\currently working on it\test\merge\Malaysia.xlsx",index = True))
        c += 1
        print("-----------------------------------------------")
    if  'Monthly'+ " " + str(name) + " " + 'demand for New Zealand in kb/d' in k["description"]:
        print(pd.DataFrame([k["description"]] + list(k.get("date").values()),["Date"] +list(k.get("date").keys())).to_excel(r"E:\GE-PROJECT_DATABASE\energy ascepts\currently working on it\test\merge\New Zealand.xlsx",index = True))
        c += 1
        print("-----------------------------------------------")
    if  'Monthly'+ " " + str(name) + " " + 'demand for Papua New Guinea in kb/d' in k["description"]:
        print(pd.DataFrame([k["description"]] + list(k.get("date").values()),["Date"] +list(k.get("date").keys())).to_excel(r"E:\GE-PROJECT_DATABASE\energy ascepts\currently working on it\test\merge\Papua New Guinea.xlsx",index = True))
        c += 1
        print("-----------------------------------------------")
    if  'Monthly'+ " " + str(name) + " " + 'demand for Papua New Guinea in kb/d' in k["description"]:
        print(pd.DataFrame([k["description"]] + list(k.get("date").values()),["Date"] +list(k.get("date").keys())).to_excel(r"E:\GE-PROJECT_DATABASE\energy ascepts\currently working on it\test\merge\Papua New Guinea.xlsx",index = True))
        c += 1
        print("-----------------------------------------------")
    if  'Monthly'+ " " + str(name) + " " + 'demand for Philippines  in kb/d' in k["description"]:
        print(pd.DataFrame([k["description"]] + list(k.get("date").values()),["Date"] +list(k.get("date").keys())).to_excel(r"E:\GE-PROJECT_DATABASE\energy ascepts\currently working on it\test\merge\Papua Philippines.xlsx",index = True))
        c += 1
        print("-----------------------------------------------")
    if  'Monthly'+ " " + str(name) + " " + 'demand for Pakistan  in kb/d' in k["description"]:
        print(pd.DataFrame([k["description"]] + list(k.get("date").values()),["Date"] +list(k.get("date").keys())).to_excel(r"E:\GE-PROJECT_DATABASE\energy ascepts\currently working on it\test\merge\Papua Pakistan.xlsx",index = True))
        c += 1
        print("-----------------------------------------------")
    if  'Monthly'+ " " + str(name) + " " + 'demand for Singapore  in kb/d' in k["description"]:
        print(pd.DataFrame([k["description"]] + list(k.get("date").values()),["Date"] +list(k.get("date").keys())).to_excel(r"E:\GE-PROJECT_DATABASE\energy ascepts\currently working on it\test\merge\Papua Singapore.xlsx",index = True))
        c += 1
        print("-----------------------------------------------") 
    if  'Monthly'+ " " + str(name) + " " + 'demand for Singapore  in kb/d' in k["description"]:
        print(pd.DataFrame([k["description"]] + list(k.get("date").values()),["Date"] +list(k.get("date").keys())).to_excel(r"E:\GE-PROJECT_DATABASE\energy ascepts\currently working on it\test\merge\Papua Singapore.xlsx",index = True))
        c += 1
        print("-----------------------------------------------") 
                   
           

    
    
    
    
    
    
# Merging Data
#Referenece(ref)  variable is used for converting data for cilent needs.    
ref = ['Angola',
 'Ivory_Coast',
 'Congo',
 'Cameroon',
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
 'South Africa'
 'Brunei',
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
 'Bosnia_and_Herzegovina',
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
 'United_Kingdom',
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
 'North_Macedonia',
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
 'Costa_Rica',
 'Cuba',
 'Curacao',
 'Dominican_Republic',
 'Ecuador',
 'Guatemala',
 'Honduras',
 'Jamaica',
 'Mexico',
 'Nicaragua',
 'Panama',
 'Peru',
 'Puerto_Rico',
 'El_Salvador',
 'Trinidad_and_Tobago',
 'Uruguay',
 'Venezuela',
 'US_Virgin_Islands',
 'UAE',
 'Bahrain',
 'Israel',
 'Iraq',
 'Iran',
 'Jordan',
 'Kuwait',
 'Oman',
 'Qatar',
 'Saudi_Arabia',
 'Syria',
 'Yemen',
 'Canada',
 'US',
 'US',
 'US',
 'US',
 'US',
 'US'
 ]




BASE_DIR = 'E:\\GE-PROJECT_DATABASE\\energy ascepts\\currently working on it\\test\\merge'
act_data = []; _columns = [] 

for i in ref:
    df = pd.read_excel(BASE_DIR + '\\' + i + '.xlsx')
    if list(df.keys()):
        act_data.append(list(df[list(df.keys())[1]]))
        _columns.append(list(df.keys())[1])


_index = list(df[list(df.keys())[0]]) 
_index = _index if len(list(zip(*act_data))) == len(_index) else _index[:len(list(zip(*act_data)))]

pd.DataFrame(list(zip(*([_index] + act_data))), columns=['Date'] + _columns
            ).to_excel(r'E:\GE-PROJECT_DATABASE\energy ascepts\currently working on it\test\Merged_xlsx\test_global_disel_demand.xlsx',index=False,sheet_name = 'test')
print("DATA IS MERGED INTO SINGLE EXCEL FILE.")


        
    
    
    
    
    
    
    





        