import json
with open(r"E:\GE_project\converted.json",'r') as file:
   main =  json.load(file)
   c = 0
for i in main.values():
    res = main["main Menu"]
# print(res)
    
    
for j in res:
    c = c + 1 
    print(res[j].replace(","," /")[::-1])
print(c)

        


