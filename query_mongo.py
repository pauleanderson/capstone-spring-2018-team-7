import json
import os
import pymongo
import re
import demjson
from bson import json_util
import datetime

connection = pymongo.MongoClient("mongodb://localhost")
db = connection.apps
android = db.android

print("Android database 'Knife Hit'")
cursor = android.find({"title":"Knife Hit"},
                   {"_id":False, "title":True, "rank":True, "country":True, "chart":True, "date":True})
for doc in cursor:
    print(doc)
    
    
apple = db.apple

print("Apple database 'Knife Hit'")
cursor = apple.find({"title":"Knife Hit"},
                   {"_id":False, "title":True, "rank":True, "country":True, "chart":True, "date":True})
for doc in cursor:
    print(doc)


