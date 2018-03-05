import json
import os
import pymongo
import re
import demjson
from bson import json_util
import datetime
import pandas as pd
#jsonData = pd.read_json(fileName, orient="records")

connection = pymongo.MongoClient("mongodb://localhost")
db = connection.apps
apple = db.apple

#data = data.replace(": undefined" , ": \"undefined\"")

cursor = apple.find({"country":"au", "chart":"free", "date":"2018-03-05"},
                   {"_id":False, "title":True, "rank":True})

df =  pd.DataFrame(list(cursor))
print(df)


'''
with open('at_gross_2018-02-21.json') as json_data:
    d = json.load(json_data)
    print(d)
'''