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

## Pick country/chart type
def pick_country(platform, country_chart):
  s = country_chart.split(" ")
  country = s[0]
  chart = s[1]
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
apple_charts = ['free', 'gross', 'new']
android_charts = ['free', 'gross', 'trend']
apple_country_charts = []
android_country_charts = []
for i in countries:
  for j in apple_charts:
    apple_country_charts.append(i+ " " + j)
  for j in android_charts:
    android_country_charts.append(i+ " " + j)


df_apple_collection = {}

for country_chart in apple_country_charts:
  df_apple_collection[country_chart] = pick_country(set_apple(), country_chart)


df_apple_pivots = {}

for key in df_apple_collection.keys():
  df_apple_pivots[key] = df_apple_collection[key].pivot_table(index = ["title", "chart"], columns = "date", values = "rank")
  df_apple_pivots[key] = df_apple_pivots[key].fillna(101)
  df_apple_pivots[key] = df_apple_pivots[key].iloc[:,df_apple_pivots[key].shape[1]-5:]
  df_apple_pivots[key] = last_five_days(df_apple_pivots[key])
  df_apple_pivots[key].reset_index(inplace = True)
  df_apple_pivots[key] = df_apple_pivots[key].loc[:,["title","delta 1:2","delta 1:3","delta 1:4","delta 1:5","delta 2:3","delta 2:4","delta 2:5","delta 3:4","delta 3:5","delta 4:5"]]

first = True

for key in df_apple_pivots.keys():
  if(first):
    df_apple = df_apple_pivots[key]
    first = False
  else:
    df_apple = pd.merge(df_apple,df_apple_pivots[key],on = ["title"],how = "outer")
df_apple = df_apple.fillna(0)
df_apple = df_apple.set_index("title")
#print(df_apple)

def printOutliers(model):
  count = 0
  for i in model:
      if(i == -1):
          print(df_apple.iloc[count])
          count = count +1
      else:
          count = count +1




'''
Android country chart
for country_chart in android_country_charts:
  df_android_collection[country_chart] = pick_country(set_android(), country_chart)
'''
#country initialzation




'''
print(pivot_au.nlargest(3,"delta rank0"))
print("")
'''



#Need to find a way to grab genre[1] and make sure its gaming.
#that code goes here
'''
#mergin data frames into one training set

#print(pivot_se.shape[0])
#pivot_Train = pivot_au.join( pivot_nz, on='title',how = "inner")
pivot_train = pd.merge(pivot_au,pivot_nz,on = ["title"],how  = "outer")
print(pivot_train)
#model
'''

outliers_fraction = 0.02
ecliptic_fit_apple = EllipticEnvelope(contamination=outliers_fraction).fit(df_apple)
ecliptic_pred_apple = ecliptic_fit_apple.predict(df_apple)
#ecliptic_pred_apple = list(set(ecliptic_pred_apple))
#print(df_apple)        

#print(ecliptic_pred_apple)


one_class_svm = svm.OneClassSVM(nu=0.1, kernel="rbf", gamma=0.1).fit(df_apple)
svm_pred_apple = one_class_svm.predict(df_apple)
#print(svm_pred_apple)
printOutliers(svm_pred_apple)

IsolationForest_apple = IsolationForest(max_samples=100,contamination = outliers_fraction).fit(df_apple)
IsolationForest_apple_pred = IsolationForest_apple.predict(df_apple)
#iprint(IsolationForest_apple_pred)
printOutliers(IsolationForest_apple_pred)

lof_apple = LocalOutlierFactor(contamination = outliers_fraction)
lof_apple_pred = lof_apple.fit_predict(df_apple)
print(lof_apple_pred)

#plot(ecliptic_fit_apple)



