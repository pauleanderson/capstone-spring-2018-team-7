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

## Pick all countries
def pull_all_countries(platform):
  return pd.DataFrame(list(platform.find()))

def unicode():
  return dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)

def pick_last_five(df):
  return df.iloc[:, len(df.columns)-5:len(df.columns)].copy()

#def find_deltas(df, number_of_deltas):
  

df1 = pick_country(set_apple(), "au")
df2 = pull_all_countries(set_apple())

#Build the pivot table
pivot = df1.pivot_table(index = "title", columns = "date", values = "rank")
pivot = pivot.fillna(101)
pivot = pick_last_five(pivot)
#print(pivot.to_string().translate(unicode()))

# to be completed
#for index, row in pivot.iterrows():
  #print (row['2018-03-04'])

def first_delta (df, row):
  return row[len(df.columns)-2]-row[len(df.columns)-1]

def all_deltas (df, row):
  number = len(df.columns)
  for i in number:
    for j in number:
      df['delta rank' + column] = row[j]-row[i]
  return df
      



pivot['delta rank1'] = pivot.apply (lambda row: all_deltas (pivot, row),axis=1)
print(pivot.to_string().translate(unicode()))
#print(pivot["delta rank1"].max())
print("")
print("")
print("")
print("The bigest positive change over last 24 hours:")
#print(pivot.loc[pivot["delta rank1"].idxmax()])
