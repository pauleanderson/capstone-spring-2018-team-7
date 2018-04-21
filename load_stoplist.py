import json
import os
import pymongo
from bson import json_util

connection = pymongo.MongoClient("mongodb://localhost")
db = connection.apps
stoplist = db.stoplist

filepath='/home/cofccapstoneteam7/capstone-spring-2018-team-7/stoplist.json'
data = open(filepath).read()
data = data.replace(": undefined",": \"undefined\"")
obj = json_util.loads(data)
app_id = stoplist.insert_many(obj)

