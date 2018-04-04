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

for key in df_apple_collection.keys():
    print("\n" +"="*40)
    print(key)
    print("-"*40)
    print(df_apple_collection[key])

'''
Android country chart
for country_chart in android_country_charts:
  df_android_collection[country_chart] = pick_country(set_android(), country_chart)
'''
#country initialzation


#Build the pivot table for au
pivot_au = df_au.pivot_table(index = ["title", "chart"], columns = "date", values = "rank")
pivot_au = pivot_au.fillna(101)
pivot_au = pivot_au.iloc[:,pivot_au.shape[1]-6:]
#print(pivot_au.to_string().translate(unicode()))
pivot_au = last_five_days(pivot_au)
pivot_au.reset_index(inplace = True)
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
pivot_nz = pivot_nz.iloc[:,pivot_nz.shape[1]-6:]
pivot_nz = last_five_days(pivot_nz)
pivot_nz.reset_index(inplace = True)
#print(pivot_nz.to_string().translate(unicode()))


#se
pivot_se = df_se.pivot_table(index = ["title", "chart"], columns = "date", values = "rank")
pivot_se = pivot_se.fillna(101)
pivot_se = pivot_se.iloc[:,pivot_se.shape[1]-6:]
pivot_se = last_five_days(pivot_se)
#print(pivot_se.to_string().translate(unicode()))

#dk 
pivot_dk = df_dk.pivot_table(index = ["title", "chart"], columns = "date", values = "rank")
pivot_dk = pivot_dk.fillna(101)
pivot_dk = pivot_dk.iloc[:,pivot_dk.shape[1]-6:]
pivot_dk = last_five_days(pivot_dk)
#print(pivot_dk.to_string().translate(unicode()))

#no 
pivot_no = df_no.pivot_table(index = ["title", "chart"], columns = "date", values = "rank")
pivot_no = pivot_no.fillna(101)
pivot_no = pivot_no.iloc[:,pivot_no.shape[1]-6:]
pivot_no = last_five_days(pivot_no)
#print(pivot_no.to_string().translate(unicode()))

#at 
pivot_at = df_at.pivot_table(index = ["title", "chart"], columns = "date", values = "rank")
pivot_at = pivot_at.fillna(101)
pivot_at = pivot_at.iloc[:,pivot_at.shape[1]-6:]
pivot_at = last_five_days(pivot_at)
#print(pivot_at.to_string().translate(unicode()))

#ph
pivot_ph = df_ph.pivot_table(index = ["title", "chart"], columns = "date", values = "rank")
pivot_ph = pivot_ph.fillna(101)
pivot_ph = pivot_ph.iloc[:,pivot_ph.shape[1]-6:]
pivot_ph = last_five_days(pivot_ph)
#print(pivot.to_string().translate(unicode()))
#print(pivot_ph.to_string().translate(unicode()))

#Need to find a way to grab genre[1] and make sure its gaming.
#that code goes here

#mergin data frames into one training set

#print(pivot_se.shape[0])
#pivot_Train = pivot_au.join( pivot_nz, on='title',how = "inner")
pivot_train = pd.merge(pivot_au,pivot_nz,on = ["title"],how  = "outer")
print(pivot_train)
#model

outliers_fraction = 0.02
ecliptic_fit_apple = EllipticEnvelope(contamination=outliers_fraction).fit(pivot_Train)
ecliptic_fit_apple.predict(pivot_Test)

one_class_svm = svm.OneClassSVM(nu=0.1, kernel="rbf", gamma=0.1)
clf.fit(pivot_Train)

#plot(ecliptic_fit_apple)



