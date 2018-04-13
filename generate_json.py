import json
from pymongo import MongoClient
import datetime
import pandas as pd

current_date = datetime.datetime.now().strftime("%Y-%m-%d")

## connect to the database
client = MongoClient('localhost', 27017)
data = client.apps

## Pick Android collections
def set_android():
  return data.android

## Pick Apple collections
def set_apple():
  return data.apple

## Select df of occurences of title in today's df type
def pick_title(platform, title, date):
  return pd.DataFrame(list(platform.find({"title":title,"date":date, "chart":"gross"})))

df_apple = pick_title(set_apple(), "Fortnite", current_date)
df_android = pick_title(set_android(), "Candy Crush Saga", current_date)

apple_countries = df_apple['country'].tolist()
apple_countries = map(str, apple_countries)
android_countries = df_android['country'].tolist()
android_countries = map(str, android_countries)
apple_ranks = df_apple['rank'].tolist()
android_ranks = df_android['rank'].tolist()

apple_countries_string = ""
android_countries_string = ""
for i in range(len(apple_countries)):
    apple_countries_string = apple_countries_string + apple_countries[i] + "- " + str(apple_ranks[i]) + "\t"
for i in range(len(android_countries)):
    android_countries_string = android_countries_string + android_countries[i] + "- " + str(android_ranks[i]) + "\t"

apple_title = str(df_apple['title'].tolist()[0])
android_title = str(df_android['title'].tolist()[0])

apple_dev = str(df_apple['developer'].tolist()[0])
android_dev = str(df_android['developer'].tolist()[0])

apple_released = str(df_apple['released'].tolist()[0])

apple_url = str(df_apple['url'].tolist()[0])
android_url = str(df_android['url'].tolist()[0])

apple_icon = str(df_apple['icon'].tolist()[0])
android_icon = "https:" + str(df_android['icon'].tolist()[0])

def generate_data (string):
    string = '{' +'\n' + '"text":"*Good morning from Cayce!* The update for today:", "attachments": [' + string[:-1]
    string = string + ']}'
    return string

def app_data (platform, icon, title, countries, developer, url, release=''):
    if (platform == "Android"):
        data = '{' + '\n' + '"title"' + ':' + '"Android Trending App",' + '\n' + \
                '"fields":' + '[' + '\n' + \
                '{' + '"title":' + '"Game"' + ',' + '"value":' + '\"' + title  + '\"' + '}' + ',' + '\n' + \
                '{' + '"title":' + '"Countries and Ranks"' + ',' + '"value":' + '\"' + countries + '\"' + '}' + ',' + '\n' + \
                '{' + '"title":' + '"Developer"' + ',' + '"value":' + '\"' + developer + '\"' + '}' + ',' + '\n' + \
                '{' + '"title":' + '"URL"' + ',' + '"value":' + '\"' + url + '\"' + '}' + '\n'+ '],' + '\n' + \
                '"image_url":' + '\"' + icon + '\"}'
    else:
        data = '{' + '\n' + '"title"' + ':' + '"Apple Trending App",' + '\n' + \
                '"fields":' + '[' + '\n' + \
                '{' + '"title":' + '"Game"' + ',' + '"value":' + '\"' + title + '\"' + '}' + ',' + '\n' + \
                '{' + '"title":' + '"Countries and Ranks"' + ',' + '"value":' + '\"' + countries + '\"' + '}' + ',' + '\n' + \
                '{' + '"title":' + '"Developer"' + ',' + '"value":' + '\"' + developer + '\"' + '}' + ',' + '\n' + \
                '{' + '"title":' + '"Release Date"' + ',' + '"value":' + '\"' + release + '\"' + '}' + ',' + '\n' + \
                '{' + '"title":' + '"URL"' + ',' + '"value":' + '\"' + url + '\"' + '}' + '\n'+ '],' + '\n' + \
                '"image_url":' + '\"' + icon + '\"' + '}'    
    return data

#TODO once the input to python is decided, we will need a function that will loop through apps like code below:
datam = ''
datam = datam + app_data("Apple", apple_icon, apple_title, apple_countries_string, apple_dev, apple_url, release=apple_released) + ','
datam = datam + app_data("Android", android_icon, android_title, android_countries_string, android_dev, android_url)


file = open('data3.json', 'w')
file.write(generate_data(datam))
file.close()

