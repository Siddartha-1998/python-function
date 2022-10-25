import json
import pandas as pd
import requests as req
# r1 = req.get('https://api.energyaspects.com/data/timeseries/?api_key=EPvbpqLCa90jVF3r&date_from=2009-01-01&date_to=2023-12-23&dataset_id=2069')
# print(eval(r1.text))
l = [] 
l1 = []
dict = {}
for i in range(2296,2310):
    
    request = ['https://api.energyaspects.com/data/timeseries/?api_key=EPvbpqLCa90jVF3r&date_from=2009-01-01&date_to=2023-12-23&dataset_id=']
    id = i
    res_1 = request[0]+str(i)
    main = req.get(res_1)
    r1 = json.loads(main.text)
    resp = r1[0]
    data = str(resp['metadata']['description'] + str(resp['data']))
    l.append(data)
for j in range(0,len(l)):
    dict['description']=l[j][:36]
    resp1= l[j][37:]
    dict['date']= resp1
    # print(dict)
    l1.append(dict)
    print(l1[0]['description'])
#     for k in l1:
#          pd.DataFrame(list(zip(list(str(eval(k.get('data')).keys())), list(str(eval(k.get('data'))).values()))),
#                             columns=['Date', str(eval(k.get('description')))]
#                                 ).to_excel(r'E:\GE-PROJECT_DATABASE\energy ascepts\currently working on it\done5.xlsx',
#                                         index=False)
#                                         # sheet_name=i.get('metadata').get('description').replace('/', '_'))
   


    
 
    