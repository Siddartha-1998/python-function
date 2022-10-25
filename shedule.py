from sched import scheduler

import pandas as pd
import requests as req
import schedule as shed
import time
import csv
import json
from re import I

import os
def sched():
    print('working')
print(sched())      
                                
    

    
    
shed.every(2).seconds.do(sched)


while True:
    shed.run_pending()
    time.sleep(1)
    