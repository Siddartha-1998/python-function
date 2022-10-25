
import json
l=[]
c = 0

with open(r'C:\Users\Techforce\Downloads\Updated nlu.md') as f:
    data = f.read()
res = [i.split('\n') for i in data.split('##')[1:]]
res_1 = [{i[0]: i[1:]} for i in res]
for j in res_1:
    for intent in j:
        c += 1
        for k in j[intent]:
            if k.strip("-"):
                main = k.strip(" -")
                l.append({"text":main,
                      "intents":intent.split(':')[-1].strip(' '),
                      "entities":[]
                      })
            
            
            
print(l)
print("count of intents",c)
with open(r'E:\NLP-main_marico1.json', mode='w') as f:
    json.dump({'rasa_nlu_data': {'Marico': l}}, f, indent=3)
            
        
        


                 
                


                 
    
                 
        
        

    
           