

#jsonData = pd.read_json(fileName, orient="records")

from pymongo import MongoClient
import pandas as pd
import sys

## connect to the database
client = MongoClient ('localhost', 27017)
data = client.apps

## start with opening data

def set_android ():
  return data.android

def set_apple ():
  return data.apple

def pick_platform(platform):
  return pd.DataFrame(list(platform.find()))

df = pick_platform(set_apple())
print df



'''
with open('at_gross_2018-02-21.json') as json_data:
    d = json.load(json_data)
    print(d)
'''