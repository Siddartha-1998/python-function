import json

with open(r"C:\Users\Techforce\Downloads\new_intents.md") as f:
    data = f.read()
l = []
# print(type(data))
res = [i.split('\n') for i in data.split('##')[1:]]
res_1 = [{i[0]: i[1:]} for i in res]
for j in res_1:
    for intent in j:
        for k in j[intent]:
            if k.strip(' -'):
                l.append({'text': k.strip(' -'),
                        'intent': intent.split(':')[-1].strip(' '),
                        'entities':[]})
# print(l)
with open(r'E:\MARICO_NLP_DATA_one.json', mode='w') as f:
    json.dump({'rasa_nlu_data': {'Marico': l}}, f, indent=3)
        