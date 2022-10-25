from doctest import FAIL_FAST
from pickle import FALSE, TRUE
import eikon as ek
import datetime as dt
import pandas as pd


ek.set_app_key('3b34e698966e4cd691f466e572ed9285d07e0915')

data = ek.get_timeseries(['CO-FOBRBY-SA'],
                        end_date=dt.datetime.now(),
                        start_date=dt.datetime.now() - dt.timedelta(days=(365*20)),
                        interval='daily')
# print(data)     
# for _key in data['CLOSE']:
#     m = _key,data["CLOSE"]
#     main = pd.DataFrame(m)
#     print(main)



# print(data["CLOSE"].,"CLOSE")
# print(data["HIGH"],"HIGH")
# print(data["LOW"],"LOW")    


# print(data["CLOSE"])
# print(type(data))
# print(data['CLOSE'].keys()[0])
# print(data['CLOSE'][data['CLOSE'].keys()[0]])
# res = [['-'.join(str(_key).strip('00:00:00').split('-')[::-1]).replace(' ', ''), data['CLOSE'][_key]] for _key in data['CLOSE'].keys()][::-1]
# print(res)

# for i in data['CLOSE'].keys():
#     m = i,data["CLOSE"]
#     print(m)

main = [['-'.join(str(_key).strip('00:00:00').split('-')[::-1]).replace(' ', ''), data['CLOSE'][_key]] for _key in data['CLOSE'].keys()][::-1]
main_1 = [['-'.join(str(_key).strip('00:00:00').split('-')[::-1]).replace(' ', ''), data['HIGH'][_key]] for _key in data['CLOSE'].keys()][::-1]
main_2 =  [['-'.join(str(_key).strip('00:00:00').split('-')[::-1]).replace(' ', ''), data['LOW'][_key]] for _key in data['CLOSE'].keys()][::-1]
main_2 =  [['-'.join(str(_key).strip('00:00:00').split('-')[::-1]).replace(' ', ''), data['LOW'][_key]] for _key in data['CLOSE'].keys()][::-1]
main_3 =  [['-'.join(str(_key).strip('00:00:00').split('-')[::-1]).replace(' ', ''), data['OPEN'][_key]] for _key in data['CLOSE'].keys()][::-1]
main_4 =  [['-'.join(str(_key).strip('00:00:00').split('-')[::-1]).replace(' ', ''), data['COUNT'][_key]] for _key in data['CLOSE'].keys()][::-1]


main_df = pd.DataFrame(main,columns=['Date', 'CLOSE'])
main_df_1 = pd.DataFrame(main_1, columns=['Date', 'HIGH'])
main_df_2 = pd.DataFrame(main_2, columns=['Date', 'LOW'])
main_df_3 = pd.DataFrame(main_3, columns=['Date', 'OPEN'])
main_df_4 = pd.DataFrame(main_4, columns=['Date', 'COUNT'])
print(main_df)
print(main_df_1)
print(main_df_2)
print(main_df_3)
print(main_df_4)
main_df.to_excel('Test_1.xlsx',index=False)
main_df_1.to_excel('Test_2.xlsx', index=False)
main_df_2.to_excel('Test_3.xlsx', index=False)
main_df_3.to_excel('Test_4.xlsx', index=False)
main_df_4.to_excel('Test_5.xlsx', index=False)


# res = [[data['CLOSE'][_key] for _key in data['CLOSE'].keys()][::-1]]
# res_1 = [['-'.join(str(_key).strip('00:00:00').split('-')[::-1]).replace(' ', '')]]

# print(res)



# res.insert(0, ['', 'Close'])
# res_df = pd.DataFrame(res, columns=['Date', 'CO-FOBRBY-SA'])
# res_df.to_excel('CO-FOBRBY-SA_python.xlsx', index=False)
# # co-fobnwc-AU


