import json
import os
import pymongo
import re
import demjson
from bson import json_util
import datetime

current_date = datetime.datetime.now().strftime("%Y-%m-%d")

dir='/home/cofccapstoneteam7/capstone-spring-2018-team-7/collect_data/android'
connection = pymongo.MongoClient("mongodb://localhost")
db = connection.apps
android = db.android
for filename in os.listdir(dir):
    filepath = dir+'/'+filename
    if filename == ".DS_Store" or filename == ".ipynb_checkpoints":
        continue
    split = re.split('_|\.',filename)
    country = split[0]
    chart = split[1]
    date = split[2]
    if date != current_date:
        continue
    data = open(filepath).read()
    data = data.replace(": undefined",": \"undefined\"")
    obj = json_util.loads(data)
    for i in range(0, len(obj)):
        obj[i]["country"] = country
        obj[i]["chart"] = chart
        obj[i]["date"] = date
        obj[i]["rank"] = i+1
    app_id = android.insert_many(obj)


dir='/home/cofccapstoneteam7/capstone-spring-2018-team-7/collect_data/apple'
connection = pymongo.MongoClient("mongodb://localhost")
db = connection.apps
apple = db.apple
for filename in os.listdir(dir):
    filepath = dir+'/'+filename
    if filename == ".DS_Store" or filename == ".ipynb_checkpoints":
        continue
    split = re.split('_|\.',filename)
    country = split[0]
    chart = split[1]
    date = split[2]
    if date != current_date:
        continue
    data = open(filepath).read()
    data = data.replace(": undefined",": \"undefined\"")
    obj = json_util.loads(data)
    for i in range(0, len(obj)):
        obj[i]["country"] = country
        obj[i]["chart"] = chart
        obj[i]["date"] = date
        obj[i]["rank"] = i+1
    app_id = apple.insert_many(obj)
