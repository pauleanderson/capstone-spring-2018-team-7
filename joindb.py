from pymongo import MongoClient
import pandas as pd
import sys
from sklearn.covariance import EllipticEnvelope
from sklearn.ensemble import IsolationForest
from sklearn.neighbors import LocalOutlierFactor
from sklearn import svm
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

def last_five_days(df):
  df['delta 1:2'] = df.apply (lambda row: delta (df, row,0,1),axis=1)
  df['delta 1:3'] = df.apply (lambda row: delta (df, row,0,2),axis=1)
  df['delta 1:4'] = df.apply (lambda row: delta (df, row,0,3),axis=1)
  df['delta 1:5'] = df.apply (lambda row: delta (df, row,0,4),axis=1)

  df['delta 2:3'] = df.apply (lambda row: delta (df, row,1,2),axis=1)
  df['delta 2:4'] = df.apply (lambda row: delta (df, row,1,3),axis=1)
  df['delta 2:5'] = df.apply (lambda row: delta (df, row,1,4),axis=1)

  df['delta 3:4'] = df.apply (lambda row: delta (df, row,2,3),axis=1)
  df['delta 3:5'] = df.apply (lambda row: delta (df, row,2,4),axis=1)

  df['delta 4:5'] = df.apply (lambda row: delta (df, row,3,4),axis=1)
  return df

def first_delta (df, row):
  return row[len(df.columns)-2]-row[len(df.columns)-1]

#country initialzation
df_au = pick_country(set_apple(), 'au')
df_nz = pick_country(set_apple(), 'nz')
df_se = pick_country(set_apple(), 'se')
df_dk = pick_country(set_apple(), 'dk')
df_no = pick_country(set_apple(), 'no')
df_at = pick_country(set_apple(), 'at')
df_ph = pick_country(set_apple(), 'ph')

#Build the pivot table
pivot_au = df_au.pivot_table(index = ["title", "chart"], columns = "date", values = "rank")
pivot_au = pivot_au[,(pivot_au.columns - 5):]
pivot_au = pivot_au.fillna(101)
#print(pivot.to_string().translate(unicode()))


pivot_au['delta rank0'] = pivot_au.apply (lambda row: first_delta (pivot_au, row),axis=1)
print(pivot_au.to_string().translate(unicode()))

#print(pivot["delta rank1"].max())

print("")
print("")
print("")
print("The 3 bigest positive change over last 4 days in australia:")
print(pivot_au.nlargest(3,"delta rank1"))
print("")

#nz 


#Build the pivot table
pivot_nz = df_nz.pivot_table(index = ["title", "chart"], columns = "date", values = "rank")
pivot_nz = pivot_nz.fillna(101)
#print(pivot.to_string().translate(unicode()))


pivot_nz['delta rank2'] = pivot_nz.apply (lambda row: first_delta (pivot_nz, row),axis=1)
print(pivot_nz.to_string().translate(unicode()))


#Build the pivot table
pivot_se = df_se.pivot_table(index = ["title", "chart"], columns = "date", values = "rank")
pivot_se = pivot_se.fillna(101)
#print(pivot.to_string().translate(unicode()))


pivot_se['delta rank3'] = pivot_se.apply (lambda row: first_delta (pivot_se, row),axis=1)
print(pivot_se.to_string().translate(unicode()))
#print(pivot["delta rank1"].max())

#dk 
#Build the pivot table
pivot_dk = df_dk.pivot_table(index = ["title", "chart"], columns = "date", values = "rank")
pivot_dk = pivot_dk.fillna(101)
#print(pivot.to_string().translate(unicode()))
pivot_dk['delta rank4'] = pivot_dk.apply (lambda row: first_delta (pivot_dk, row),axis=1)
print(pivot_dk.to_string().translate(unicode()))
#print(pivot["delta rank1"].max())

#no 
#Build the pivot table
pivot_no = df_no.pivot_table(index = ["title", "chart"], columns = "date", values = "rank")
pivot_no = pivot_no.fillna(101)
#print(pivot.to_string().translate(unicode()))
pivot_no['delta rank5'] = pivot_no.apply (lambda row: first_delta (pivot_no, row),axis=1)
print(pivot_no.to_string().translate(unicode()))
#print(pivot["delta rank1"].max())


#at 
#Build the pivot table
pivot_at = df_at.pivot_table(index = ["title", "chart"], columns = "date", values = "rank")
pivot_at = pivot_at.fillna(101)
#print(pivot.to_string().translate(unicode()))
pivot_at['delta rank6'] = pivot_at.apply (lambda row: first_delta (pivot_at, row),axis=1)
print(pivot_at.to_string().translate(unicode()))
#print(pivot["delta rank1"].max())

#ph
#Build the pivot table
pivot_ph = df_ph.pivot_table(index = ["title", "chart"], columns = "date", values = "rank")
pivot_ph = pivot_ph.fillna(101)
#print(pivot.to_string().translate(unicode()))
pivot_ph['delta rank7'] = pivot_ph.apply (lambda row: first_delta (pivot_ph, row),axis=1)
print(pivot_ph.to_string().translate(unicode()))
#print(pivot["delta rank1"].max())
#print(pivot.loc[pivot["delta rank1"].idxmax()])


#Need to find a way to grab genre[1] and make sure its gaming.
#that code goes here


#model

outliers_fraction = 0.02
ecliptic_fit_apple = EllipticEnvelope(contamination=outliers_fraction).fit(pivot_Train)
ecliptic_fit_apple.predict(pivot_Test)

one_class_svm = svm.OneClassSVM(nu=0.1, kernel="rbf", gamma=0.1)
clf.fit(pivot_Train)

#plot(ecliptic_fit_apple)



