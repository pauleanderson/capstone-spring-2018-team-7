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

df_apple = pick_title(set_apple(), "Knife Hit", current_date)
df_android = pick_title(set_android(), "Knife Hit", current_date)

apple_countries = df_apple["country"].tolist()
android_countries = df_android["country"].tolist()
apple_ranks = df_apple["rank"].tolist()
android_ranks = df_android["rank"].tolist()

print(apple_countries)
print(apple_ranks)
print(android_countries)
print(android_ranks)

def generate_data (string):
    string = '{' +'\n' + '"text":"*Cayce heils you!* The update for today:", "attachments": [' + string[:-1]
    string = string + ']}'
    return string

def app_data (icon, title, country, rank, chart, developer, url):
    data = '{' +'\n' + '"title": "' + title + '", "text": "Highest Rank Country: ' + country + '\t Current Rank: ' + rank + '\t Chart: ' + chart + '\t Developer: ' + developer + '", "thumb_url": "' + url +  '"},'
    return data

#TODO once the input to python is decided, we will need a function that will loop through apps like code below:
datam = ''
for i in range (0,3):
    datam = datam+app_data('icon', 'Dragon Times', 'AU', '100', 'Free', 'crazy_developer', 'https://lh3.googleusercontent.com/lZhL5smuoS8EqylXKUgv5tN7V9jlSUT2txzyHYHcIBDwTLkKjDGmuEXDS5N6YB5Oag=w340')

file = open('data2.json', 'w')
#file.write(generate_data(app_data('icon', 'Dragon Times', 'AU', '100', 'Free', 'crazy_developer', 'https://lh3.googleusercontent.com/lZhL5smuoS8EqylXKUgv5tN7V9jlSUT2txzyHYHcIBDwTLkKjDGmuEXDS5N6YB5Oag=w340')))
file.write(generate_data(datam))
file.close()
