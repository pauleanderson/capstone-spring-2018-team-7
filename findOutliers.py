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
import datetime

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

def set_stoplist():
  return data.stoplist

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

#adding all country related app store data to a dataframe
for i in countries:
    apple_country_charts.append(pick_country(set_apple(),i))
    android_country_charts.append(pick_country(set_android(),i))

#calculating the permutations of delta change and adding them to the delta frame
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
  df_android_pivots[i] = df_android_pivots[i].fillna(501)
  df_android_pivots[i] = df_android_pivots[i].iloc[:,df_android_pivots[i].shape[1]-5:]
  df_android_pivots[i] = last_five_days(df_android_pivots[i])
  df_android_pivots[i].reset_index(inplace = True)
  df_android_pivots[i] = df_android_pivots[i].loc[:,["title","delta 1:2","delta 1:3","delta 1:4","delta 1:5","delta 2:3","delta 2:4","delta 2:5","delta 3:4","delta 3:5","delta 4:5"]] 


#cleaning and merging the deltas into a new dataframe
first = True
for i in range(len(df_apple_pivots)):
  if(first):
    df_apple = df_apple_pivots[i]
    first = False
  else:
    df_apple = pd.merge(df_apple,df_apple_pivots[i],on = ["title"],how = "outer")

df_apple = df_apple.fillna(0)
df_apple = df_apple.set_index("title")


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

#method for appending outliers (-1) to a list
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


#Isolation forest code
outliers_fraction = 0.0025
IsolationForest_apple = IsolationForest(max_samples=100,contamination = outliers_fraction).fit(df_apple)
IsolationForest_apple_pred = IsolationForest_apple.predict(df_apple)

IsolationForest_android = IsolationForest(max_samples=100,contamination = outliers_fraction).fit(df_android)
IsolationForest_android_pred = IsolationForest_android.predict(df_android)

printOutliers(IsolationForest_apple_pred,"apple")
printOutliers(IsolationForest_android_pred,"android")



#finding the best outlier
df_apple['max'] = df_apple.max(axis = 1)
df_android['max'] = df_android.max(axis = 1)

df_apple_outliers = df_apple.iloc[outliers_apple_i,:]
df_android_outliers = df_android.iloc[outliers_android_i,:]

stoplist = pd.DataFrame(list(set_stoplist().find({},{"title":1,"_id":0})))
stoplist = stoplist["title"].tolist()



df_apple_outliers = df_apple_outliers[~df_apple_outliers.index.isin(stoplist)]
df_android_outliers = df_android_outliers[~df_android_outliers.index.isin(stoplist)]

df_apple_outliers = df_apple_outliers.sort_values(by = ['max'], ascending = False)
df_android_outliers = df_android_outliers.sort_values(by = ['max'], ascending = False)

appleOutlier = ""
androidOutlier = ""

if(len(df_apple_outliers) > 0): 
  appleOutlier = df_apple_outliers.index[0]

if(len(df_android_outliers) > 0): 
  androidOutlier = df_android_outliers.index[0]



#coding json for slack bot output
current_date = datetime.datetime.now().strftime("%Y-%m-%d")
apple_title = ""
apple_dev = ""
apple_released = ""
apple_url = ""
apple_icon = ""
apple_countries_string = ""

android_title = ""
android_dev = ""
android_url = ""
android_icon = ""
android_countries_string = ""


#Json formatting
def pick_title(platform, title, date):
  return pd.DataFrame(list(platform.find({"title":title,"date":date, "chart":"gross"})))



if(appleOutlier != ""):
  df_apple = pick_title(set_apple(), appleOutlier, current_date)
  apple_countries = df_apple['country'].tolist()
  apple_countries = map(str, apple_countries)
  apple_ranks = df_apple['rank'].tolist()
  apple_countries_string = ""

  for i in range(len(apple_countries)):
    apple_countries_string = apple_countries_string + apple_countries[i] + ": " + str(apple_ranks[i]) + "  "

  apple_countries_string = apple_countries_string.replace("au", "Australia")
  apple_countries_string = apple_countries_string.replace("nz", "New Zealand")
  apple_countries_string = apple_countries_string.replace("se", "Sweden")
  apple_countries_string = apple_countries_string.replace("dk", "Denmark")
  apple_countries_string = apple_countries_string.replace("no", "Norway")
  apple_countries_string = apple_countries_string.replace("at", "Austria")
  apple_countries_string = apple_countries_string.replace("ph", "Phillipines")
  apple_title = str(df_apple['title'].tolist()[0])
  apple_dev = str(df_apple['developer'].tolist()[0])
  apple_released = str(df_apple['released'].tolist()[0])
  apple_url = str(df_apple['url'].tolist()[0])
  apple_icon = str(df_apple['icon'].tolist()[0])

if(androidOutlier != ""):
  df_android = pick_title(set_android(), androidOutlier, current_date)
  android_countries = df_android['country'].tolist()
  android_countries = map(str, android_countries)
  android_ranks = df_android['rank'].tolist()
  android_countries_string = ""
  for i in range(len(android_countries)):
    android_countries_string = android_countries_string + android_countries[i] + ": " + str(android_ranks[i]) + "  "

  android_countries_string = android_countries_string.replace("au", "Australia")
  android_countries_string = android_countries_string.replace("nz", "New Zealand")
  android_countries_string = android_countries_string.replace("se", "Sweden")
  android_countries_string = android_countries_string.replace("dk", "Denmark")
  android_countries_string = android_countries_string.replace("no", "Norway")
  android_countries_string = android_countries_string.replace("at", "Austria")
  android_countries_string = android_countries_string.replace("ph", "Phillipines")

  android_title = str(df_android['title'].tolist()[0])
  android_dev = str(df_android['developer'].tolist()[0])
  android_url = str(df_android['url'].tolist()[0])
  android_icon = "https:" + str(df_android['icon'].tolist()[0])


def generate_data (string):
    string = '{' +'\n' + '"text":"*Good morning from Cayce!* The update for today:", "attachments": [' + string
    string = string + ']}'
    return string

def app_data (platform, icon, title, countries, developer, url, release=''):
    if (platform == "Android" and title != ""):
        data = '{' + '\n' + '"title"' + ':' + '"Android Trending App",' + '\n' + \
                '"fields":' + '[' + '\n' + \
                '{' + '"title":' + '"Game"' + ',' + '"value":' + '\"' + title  + '\"' + '}' + ',' + '\n' + \
                '{' + '"title":' + '"Countries and Top Grossing Ranks"' + ',' + '"value":' + '\"' + countries + '\"' + '}' + ',' + '\n' + \
                '{' + '"title":' + '"Developer"' + ',' + '"value":' + '\"' + developer + '\"' + '}' + ',' + '\n' + \
                '{' + '"title":' + '"URL"' + ',' + '"value":' + '\"' + url + '\"' + '}' + '\n'+ '],' + '\n' + \
                '"image_url":' + '\"' + icon + '\"' + '}'
    elif(platform == "Android" and title == ""):
        data = '{' + '\n' + '"title"' + ':' + '"Android Trending App",' + '\n' + \
                '"fields":' + '[' + '\n' + \
                '{' + '"title":' + '"Update:"' + ',' + '"value":' + '\"' + "No trending app today" + '\"' + '}' + '\n'+ '],' + '\n' + '}'
    elif(platform == "Apple" and title != ""):
        data = '{' + '\n' + '"title"' + ':' + '"Apple Trending App",' + '\n' + \
                '"fields":' + '[' + '\n' + \
                '{' + '"title":' + '"Game"' + ',' + '"value":' + '\"' + title + '\"' + '}' + ',' + '\n' + \
                '{' + '"title":' + '"Countries and Top Grossing Ranks"' + ',' + '"value":' + '\"' + countries + '\"' + '}' + ',' + '\n' + \
                '{' + '"title":' + '"Developer"' + ',' + '"value":' + '\"' + developer + '\"' + '}' + ',' + '\n' + \
                '{' + '"title":' + '"Release Date"' + ',' + '"value":' + '\"' + release + '\"' + '}' + ',' + '\n' + \
                '{' + '"title":' + '"URL"' + ',' + '"value":' + '\"' + url + '\"' + '}' + '\n'+ '],' + '\n' + \
                '"image_url":' + '\"' + icon + '\"' + '}' 
    elif(platform == "Apple" and title == ""):  
        data = '{' + '\n' + '"title"' + ':' + '"Apple Trending App",' + '\n' + \
                '"fields":' + '[' + '\n' + \
                '{' + '"title":' + '"Update:"' + ',' + '"value":' + '\"' + "No trending app today" + '\"' + '}' + '\n'+ '],' + '\n' + '}'
    return data

#TODO once the input to python is decided, we will need a function that will loop through apps like code below:
datam = ''
datam = datam + app_data("Apple", apple_icon, apple_title, apple_countries_string, apple_dev, apple_url, release=apple_released) + ','
datam = datam + app_data("Android", android_icon, android_title, android_countries_string, android_dev, android_url)


file = open('slack.json', 'w')
file.write(generate_data(datam))
file.close()







