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



data.execute('Use data1','desc main1')
for i in data:
    
    print(list(i))

