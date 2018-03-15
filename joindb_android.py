from pymongo import MongoClient
import pandas as pd
import sys

##___________________helper functions____________________

## connect to the database
client = MongoClient ('localhost', 27017)
data = client.apps

## pick the collection
def set_android ():
  return data.android

def set_apple ():
  return data.apple

## Pick 1 country
def pick_country(platform, country):
  return pd.DataFrame(list(platform.find({"country":country})))

## Pick all countries
def pull_all_countries(platform):
  return pd.DataFrame(list(platform.find()))

## Translate unicode
def unicode():
  return dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)

## pick ranks for the last 5 days
def pick_last_five(df):
  return df.iloc[:, len(df.columns)-5:len(df.columns)].copy()

## Build pivot table
def pivot_table(df):
  pivot = df.pivot_table(index = ["title", "chart"], columns = "date", values = "rank")
  pivot = pivot.fillna(101)
  pivot = pick_last_five(pivot)
  return pivot
  

df1 = pick_country(set_apple(), "au")

#Build the pivot table
pivot = pivot_table(df1)
#print(pivot.to_string().translate(unicode()))

# to be completed
#for index, row in pivot.iterrows():
  #print (row['2018-03-04'])

def first_delta (df, row):
  return row[len(df.columns)-2]-row[len(df.columns)-1]

def delta (df, row, column1, column2):
  return row[column2]-row[column1]    

pivot['delta 1:2'] = pivot.apply (lambda row: delta (pivot, row,0,1),axis=1)
pivot['delta 1:3'] = pivot.apply (lambda row: delta (pivot, row,0,2),axis=1)
pivot['delta 1:4'] = pivot.apply (lambda row: delta (pivot, row,0,3),axis=1)
pivot['delta 1:5'] = pivot.apply (lambda row: delta (pivot, row,0,4),axis=1)

pivot['delta 2:3'] = pivot.apply (lambda row: delta (pivot, row,1,2),axis=1)
pivot['delta 2:4'] = pivot.apply (lambda row: delta (pivot, row,1,3),axis=1)
pivot['delta 2:5'] = pivot.apply (lambda row: delta (pivot, row,1,4),axis=1)

pivot['delta 3:4'] = pivot.apply (lambda row: delta (pivot, row,2,3),axis=1)
pivot['delta 3:5'] = pivot.apply (lambda row: delta (pivot, row,2,4),axis=1)

pivot['delta 4:5'] = pivot.apply (lambda row: delta (pivot, row,3,4),axis=1)

print(pivot.to_string().translate(unicode()))
#print(pivot["delta rank1"].max())
print("")
print("")
print("")
print("The bigest positive change over last 24 hours:")
#print(pivot.loc[pivot["delta rank1"].idxmax()])
