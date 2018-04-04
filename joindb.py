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
  
def delta (df, row, column1, column2):
  return row[column2]-row[column1] 


#country initialzation
df_au = pick_country(set_apple(), 'au')
df_nz = pick_country(set_apple(), 'nz')
df_se = pick_country(set_apple(), 'se')
df_dk = pick_country(set_apple(), 'dk')
df_no = pick_country(set_apple(), 'no')
df_at = pick_country(set_apple(), 'at')
df_ph = pick_country(set_apple(), 'ph')

#Build the pivot table for au
pivot_au = df_au.pivot_table(index = ["title", "chart"], columns = "date", values = "rank")
pivot_au = pivot_au.fillna(101)
pivot_au = pivot_au.iloc[:,pivot_au.shape[1]-6:]
#print(pivot_au.to_string().translate(unicode()))
pivot_au = last_five_days(pivot_au)
print(pivot_au.to_string().translate(unicode()))

'''
print("")
print("")
print("")
print("The 3 bigest positive change over last 4 days in australia:")
print(pivot_au.nlargest(3,"delta rank0"))
print("")
'''

#nz 
pivot_nz = df_nz.pivot_table(index = ["title", "chart"], columns = "date", values = "rank")
pivot_nz = pivot_nz.fillna(101)
pivot_nz = pivot_au.iloc[:,pivot_nz.shape[1]-6:]
#print(pivot_nz.to_string().translate(unicode()))


#se
pivot_se = df_se.pivot_table(index = ["title", "chart"], columns = "date", values = "rank")
pivot_se = pivot_se.fillna(101)
pivot_se = pivot_se.iloc[:,pivot_se.shape[1]-6:]
#print(pivot_se.to_string().translate(unicode()))

#dk 
pivot_dk = df_dk.pivot_table(index = ["title", "chart"], columns = "date", values = "rank")
pivot_dk = pivot_dk.fillna(101)
pivot_dk = pivot_dk.iloc[:,pivot_dk.shape[1]-6:]
#print(pivot_dk.to_string().translate(unicode()))

#no 
pivot_no = df_no.pivot_table(index = ["title", "chart"], columns = "date", values = "rank")
pivot_no = pivot_no.fillna(101)
pivot_no = pivot_no.iloc[:,pivot_no.shape[1]-6:]
#print(pivot_no.to_string().translate(unicode()))

#at 
pivot_at = df_at.pivot_table(index = ["title", "chart"], columns = "date", values = "rank")
pivot_at = pivot_at.fillna(101)
pivot_at = pivot_at.iloc[:,pivot_at.shape[1]-6:]
#print(pivot_at.to_string().translate(unicode()))

#ph
pivot_ph = df_ph.pivot_table(index = ["title", "chart"], columns = "date", values = "rank")
pivot_ph = pivot_ph.fillna(101)
pivot_ph = pivot_ph.iloc[:,pivot_ph.shape[1]-6:]
#print(pivot.to_string().translate(unicode()))
#print(pivot_ph.to_string().translate(unicode()))

#Need to find a way to grab genre[1] and make sure its gaming.
#that code goes here



#model

outliers_fraction = 0.02
ecliptic_fit_apple = EllipticEnvelope(contamination=outliers_fraction).fit(pivot_Train)
ecliptic_fit_apple.predict(pivot_Test)

one_class_svm = svm.OneClassSVM(nu=0.1, kernel="rbf", gamma=0.1)
clf.fit(pivot_Train)

#plot(ecliptic_fit_apple)



