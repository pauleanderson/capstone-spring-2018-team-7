from pymongo import MongoClient
import pandas as pd
import sys
from sklearn.covariance import EllipticEnvelope
from sklearn.ensemble import IsolationForest
from sklearn.neighbors import LocalOutlierFactor
from pymongo import MongoClient
import pandas as pd
import sys

## connect to the database
client = MongoClient ('localhost', 27017)
data = client.apps

## start with opening data

## Pick Android collections
def set_android ():
  return data.android

## Pick Apple collections
def set_apple ():
  return data.apple

## Pick country
def pick_country(platform, country):
  return pd.DataFrame(list(platform.find({"country":country})))

## Pick all countries
def pull_all_countries(platform):
  return pd.DataFrame(list(platform.find()))

## Translate Unicode
def unicode():
  return dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)


df1 = pick_country(set_apple(), 'au')

#Build the pivot table
pivot = df1.pivot_table(index = ["title", "chart"], columns = "date", values = "rank")
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
print("The 3 bigest positive change over last 4 days in australia:")
print(pivot.nlargest(3,"delta rank1"))
print(len(pivot))
print("")
#print(pivot.loc[pivot["delta rank1"].idxmax()])

#


#grabing the games from the data and Aggregating it into a single table.

dfAll = pull_all_countries(set_apple())
pivotAll = dfAll.pivot_table(index = ["title"], columns = "date", values = "rank")
pivotAll = pivot.fillna(100)
pivotAll['delta rank1'] = pivotAll.apply (lambda row: first_delta (pivotAll, row),axis=1)
print(pivotAll)
#pivotAll = pivotAll[["delta rank2"]]
#print(pivotAll)
#print(pivotAll.nlargest(3,"delta rank2"))
#print(len(pivotAll))

#Need to find a way to grab genre[1] and make sure its gaming.
#that code goes here


#ecliptic model

outliers_fraction = 0.02
ecliptic_fit_apple = EllipticEnvelope(contamination=outliers_fraction).fit(pivotAll)
#ecliptic_fit_apple.predict()

#plot(ecliptic_fit_apple)



