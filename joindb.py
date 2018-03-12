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


df1 = pick_country(set_android(), "au")

#Build the pivot table
pivot = df1.pivot_table(index = ["title", "chart", "country"], columns = "date", values = "rank")
pivot = pivot.fillna(100)
#print(pivot.to_string().translate(unicode()))

# to be completed
#for index, row in pivot.iterrows():
  #print (row['2018-03-04'])

def first_delta (df, row):
  return row[len(df.columns)-2]-row[len(df.columns)-1]



pivot['delta rank1'] = pivot.apply (lambda row: first_delta (pivot, row),axis=1)
print(pivot.to_string().translate(unicode()))
#print(pivot["delta rank1"].max())
print("")
print("")
print("")
print("The bigest positive change over last 24 hours:")
print(pivot.loc[pivot["delta rank1"].idxmax()])
