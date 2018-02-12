from pymongo import MongoClient
import pandas as pd

##connect to you database
client = MongoClient('localhost',27017)

##database name and collection name
db=client.FirstPractice
games = db.games
score = games.find_one({'score':4.5})
##print(score)

scores = games.find({'score':3.5})
##for score in scores:
##    print(score)

##need to finish here
df = pd.DataFrame(list(games.find()))
print(df.to_string())
