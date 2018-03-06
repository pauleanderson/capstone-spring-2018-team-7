from pymongo import MongoClient
import pandas as pd
import sys

## connect to the database
client = MongoClient ('localhost', 27017)
data = client.apps

## start with Android data

def pick_platform (db, platform):
  return db.platform

android = pick_platform(data.android)
df = pd.DataFrame(list(android.find({"country":"au"})))
non_pbm_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)

pivot = df.pivot_table(index = "appId", columns = "date", values = "rank")
print(pivot.to_string().translate(non_pbm_map))



