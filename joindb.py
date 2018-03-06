from pymongo import MongoClient
import pandas as pd
import sys

## connect to the database
client = MongoClient ('localhost', 27017)
data = client.apps

## start with Android data

def set_android ():
  return data.android

def set_apple ():
  return data.apple

def pick_country(platform, country):
  return pd.DataFrame(list(platform.find({"country":country})))

android = set_android()
df = pick_country(android, "au")
non_pbm_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)

pivot = df.pivot_table(index = "appId", columns = "date", values = "rank")
print(pivot.to_string().translate(non_pbm_map))



