from dataclasses import dataclass
from mysql.connector import connection
import pickle

# with open('credentials_new1.pickle', mode='rb') as f:
#     creds = pickle.load(f)
    
        
# conn = connection.MySQLConnection(username=creds['user_name'],
#                                   password=creds['password'],
#                                   host='localhost'

conn = connection.MySQLConnection(username="kowshikg",
                                  password = "Siddu1998",
                                  host = "localhost")
print("connection is ok",conn)

data = conn.cursor()
l = ["SHIPING DATA","NC/0022767","NC/0022767",12336278]
input = []
# for main in l:
#     m1 = (main)
#     print(m1)
query1 = ('USE data1','create table GREAT-EASTERN_SHIPPING(_data INTEGER,INVOICE-NO INTEGER,INVOICE VARCHAR(1001),API DATA VARCHAR(100))', 'INSERT INTO data (_id, name) VALUES(100108,"sid")')
data.execute(query1)
conn.commit()   





