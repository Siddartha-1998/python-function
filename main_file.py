from mysql.connector import connection
import pickle


with open('credentials_new.pickle', mode='rb') as f:
    creds = pickle.load(f)
        
conn = connection.MySQLConnection(username=creds['user_name'],
                                  password=creds['password'],
                                  host='localhost')
# print(conn)
data = conn.cursor()
data.execute("CREATE DATABASE GE_project_one")
# data.execute("Show databases")
# print(list(data))

# l = ["SHIPING DATA","NC/0022767","NC/0022767",12336278]
# input = []
# for data in l:
#     data.execute("USE GE_project_one")
# query = "CREATE TABLE project_1 (_id INTEGER, name VARCHAR(1000))"
# # query ='SELECT * FROM project_1;'
# query = 'INSERT INTO project_1(_id,name)VALUES(100108,"siddartha")'
# query = 'select*from project_1'
# data.execute(query)

# data.execute("USE GE_project_one")
# query = "CREATE TABLE project_1 (_id INTEGER, name VARCHAR(1000))"
# # query ='SELECT * FROM project_1;'
# query = 'INSERT INTO project_1(_id,name)VALUES(100108,"siddartha")'
# query = 'select*from project_1'
# data.execute(query)
# print(data)
# for i in data:
#     print(i)


conn.commit()

# data.close()
# conn.close()
