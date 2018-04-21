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
import csv

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

## Pick country/chart type
def pick_country(platform, country):
  chart = 'gross'
  return pd.DataFrame(list(platform.find({"country":country,"chart":chart})))

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

#countries_list
countries = ['au', 'nz', 'se', 'dk', 'no', 'at', 'ph']
apple_charts =  'gross'
android_charts = 'gross'
apple_country_charts = []
android_country_charts = []

for i in countries:
    apple_country_charts.append(pick_country(set_apple(),i))
    android_country_charts.append(pick_country(set_android(),i))

df_apple_pivots = [None]*6
for i in range(len(apple_country_charts)-1):
  df_apple_pivots[i] = apple_country_charts[i].pivot_table(index = "title",columns = "date",values = "rank")
  df_apple_pivots[i] = df_apple_pivots[i].fillna(101)
  df_apple_pivots[i] = df_apple_pivots[i].iloc[:,df_apple_pivots[i].shape[1]-5:]
  df_apple_pivots[i] = last_five_days(df_apple_pivots[i])
  df_apple_pivots[i].reset_index(inplace = True)
  df_apple_pivots[i] = df_apple_pivots[i].loc[:,["title","delta 1:2","delta 1:3","delta 1:4","delta 1:5","delta 2:3","delta 2:4","delta 2:5","delta 3:4","delta 3:5","delta 4:5"]]

df_android_pivots = [None]*6
for i in range(len(android_country_charts)-1):
  df_android_pivots[i] = android_country_charts[i].pivot_table(index = "title",columns = "date",values = "rank")
  df_android_pivots[i] = df_android_pivots[i].fillna(101)
  df_android_pivots[i] = df_android_pivots[i].iloc[:,df_android_pivots[i].shape[1]-5:]
  df_android_pivots[i] = last_five_days(df_android_pivots[i])
  df_android_pivots[i].reset_index(inplace = True)
  df_android_pivots[i] = df_android_pivots[i].loc[:,["title","delta 1:2","delta 1:3","delta 1:4","delta 1:5","delta 2:3","delta 2:4","delta 2:5","delta 3:4","delta 3:5","delta 4:5"]] 



first = True
#print(df_apple_pivots)
for i in range(len(df_apple_pivots)):
  if(first):
    df_apple = df_apple_pivots[i]
    first = False
  else:
    df_apple = pd.merge(df_apple,df_apple_pivots[i],on = ["title"],how = "outer")

df_apple = df_apple.fillna(0)
df_apple = df_apple.set_index("title")
#print(df_apple)

first = True

for i in range(len(df_android_pivots)):
  if(first):
    df_android = df_android_pivots[i]
    first = False
  else:
    df_android = pd.merge(df_android,df_android_pivots[i],on = ["title"],how = "outer")

df_android = df_android.fillna(0)
df_android= df_android.set_index("title")
outliers_apple =[]
outliers_android = []
outliers_apple_i =[]
outliers_android_i = []

def printOutliers(model,ios):

  if(ios == "apple"):
    for i in range(len(model)):
      if(model[i] == -1):
          #print(df_apple.index[count])
          outliers_apple.append(df_apple.index[i])
          outliers_apple_i.append(i)
  else:
      for i in range(len(model)):
        if(model[i] == -1):
          #print(df_android.index[count])
          outliers_android.append(df_android.index[i])
          outliers_android_i.append(i)





outliers_fraction = 0.0025
IsolationForest_apple = IsolationForest(max_samples=100,contamination = outliers_fraction).fit(df_apple)
IsolationForest_apple_pred = IsolationForest_apple.predict(df_apple)

IsolationForest_android = IsolationForest(max_samples=100,contamination = outliers_fraction).fit(df_android)
IsolationForest_android_pred = IsolationForest_android.predict(df_android)
#iprint(IsolationForest_apple_pred)

printOutliers(IsolationForest_apple_pred,"apple")
printOutliers(IsolationForest_android_pred,"android")

#print(outliers_apple)

#print(outliers_android)

df_apple['max'] = df_apple.max(axis = 1)
df_android['max'] = df_android.max(axis = 1)

df_apple_outliers = df_apple.iloc[outliers_apple_i,:]
df_android_outliers = df_android.iloc[outliers_android_i,:]

stoplist = pd.read_csv("/home/cofccapstoneteam7/capstone-spring-2018-team-7/stoplist.csv",header = None,names = ["title"])
stoplist = str(stoplist["title"].tolist())

df_apple_outliers = df_apple_outliers[~df_apple_outliers.index.isin(stoplist)]
df_android_outliers = df_android_outliers[~df_android_outliers.index.isin(stoplist)]

df_apple_outliers = df_apple_outliers.sort_values(by = ['max'], ascending = False)
df_android_outliers = df_android_outliers.sort_values(by = ['max'], ascending = False)


if(len(df_apple_outliers) > 0): 
  appleOutlier = df_apple_outliers.index[0]
  print(appleOutlier)

if(len(df_android_outliers) > 0): 
  androidOutlier = df_android_outliers.index[0]
  print(androidOutlier)



 





