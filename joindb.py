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

def pick_country(platform, country):
  return pd.DataFrame(list(platform.find({"country":country})))

def unicode():
  return dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)

df = pick_country(set_apple(), "au")


pivot = df.pivot_table(index = "appId", columns = "date", values = "rank")
print(pivot.to_string().translate(unicode()))



