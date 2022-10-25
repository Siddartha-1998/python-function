import json
import pandas as pd
import requests as req


class overloaded():
    def db_overloaded():
        try:
            r1 = req.get('https://api.energyaspects.com/data/timeseries/?api_key=EPvbpqLCa90jVF3r&date_from=2009-01-01&date_to=2023-12-23&dataset_id=2069')
            r2 = req.get('https://api.energyaspects.com/data/timeseries/?api_key=EPvbpqLCa90jVF3r&date_from=2009-01-01&date_to=2023-12-23&dataset_id=2024')
            r3 = req.get('https://api.energyaspects.com/data/timeseries/?api_key=EPvbpqLCa90jVF3r&date_from=2009-01-01&date_to=2023-12-23&dataset_id=1940')
            r4 = req.get('https://api.energyaspects.com/data/timeseries/?api_key=EPvbpqLCa90jVF3r&date_from=2009-01-01&date_to=2023-12-23&dataset_id=1934')
            r5 = req.get('https://api.energyaspects.com/data/timeseries/?api_key=EPvbpqLCa90jVF3r&date_from=2009-01-01&date_to=2023-12-23&dataset_id=1935')
            r6= req.get('https://api.energyaspects.com/data/timeseries/?api_key=EPvbpqLCa90jVF3r&date_from=2009-01-01&date_to=2023-12-23&dataset_id=1936')
            


            rE1 = eval(r1.text)
            rE2 = eval(r2.text)
            rE3 = eval(r3.text)
            rE4 = eval(r4.text)
            rE5 = eval(r5.text)
            rE6 = eval(r6.text)
            print(rE1)
             
            
            for i in rE1:
                pd.DataFrame(list(zip(list(i.get('data').keys()), list(i.get('data').values()))),
                            columns=['Date', i.get('metadata').get('description')]
                                ).to_excel(r'E:\GE-PROJECT_DATABASE\energy ascepts\currently working on it\Oil products\Global disel demand\global disel demand Middle EAST.xlsx',
                                        index=False,
                                        sheet_name=i.get('metadata').get('description').replace('/', '_'))
            for j in rE2:
                pd.DataFrame(list(zip(list(j.get('data').keys()), list(j.get('data').values()))),
                            columns=['Date', j.get('metadata').get('description')]
                                ).to_excel(r'E:\GE-PROJECT_DATABASE\energy ascepts\currently working on it\Oil products\Global disel demand\global disel demand Minor Middle Eastsx', 
                                        index=False,
                                        sheet_name=j.get('metadata').get('description').replace('/', '_'))
            for k in rE3:
                 pd.DataFrame(list(zip(list(k.get('data').keys()), list(k.get('data').values()))),
                            columns=['Date', k.get('metadata').get('description')]
                                ).to_excel(r'E:\GE-PROJECT_DATABASE\energy ascepts\currently working on it\Oil products\Global disel demand\global disel demand Canada.xlsx', 
                                        index=False,
                                        sheet_name=k.get('metadata').get('description').replace('/', '_'))
            for m in rE4:
                 pd.DataFrame(list(zip(list(m.get('data').keys()), list(m.get('data').values()))),
                            columns=['Date', m.get('metadata').get('description')]
                                ).to_excel(r'E:\GE-PROJECT_DATABASE\energy ascepts\currently working on it\Oil products\Global disel demand\global disel demand PADD1 .xlsx', 
                                        index=False,
                                        sheet_name=m.get('metadata').get('description').replace('/', '_'))
            for n in rE5:
                 pd.DataFrame(list(zip(list(n.get('data').keys()), list(n.get('data').values()))),
                            columns=['Date', n.get('metadata').get('description')]
                                ).to_excel(r'E:\GE-PROJECT_DATABASE\energy ascepts\currently working on it\Oil products\Global disel demand\global disel demand PADD2 .xlsx', 
                                        index=False,
                                        sheet_name=j.get('metadata').get('description').replace('/', '_'))
            for l in rE6:
                pd.DataFrame(list(zip(list(l.get('data').keys()), list(l.get('data').values()))),
                            columns=['Date', l.get('metadata').get('description')]
                                ).to_excel(r'E:\GE-PROJECT_DATABASE\energy ascepts\currently working on it\Oil products\Global disel demand\global disel demand PADD3   .xlsx', 
                                        index=False,
                                        sheet_name=l.get('metadata').get('description').replace('/', '_'))
        except:
            print('Data completed you can check')
    print(db_overloaded())
 
