from pymongo import MongoClient
import pandas as pd
import sys
from sklearn.covariance import EllipticEnvelope
from sklearn.ensemble import IsolationForest
from sklearn.neighbors import LocalOutlierFactor

## connect to the database
client = MongoClient ('localhost', 27017)
data = client.apps

## opening data
def set_android ():
  return data.android

def set_apple ():
  return data.apple

def pick_platform(platform):
  return pd.DataFrame(list(platform.find()))

def pick_country(platform, country):
  return pd.DataFrame(list(platform.find({"country":country})))


'''
Apple Version

apple_df = pick_platform(set_apple())
pivot = apple_df.pivot_table(index = "appId", columns = "date", values = "rank")
'''

#android Version
android_au_df = pick_country(set_android(),"au")
#print android_au_df
pivot = android_au_df.pivot_table(index = "title", columns = "date", values = "rank")
#print pivot


n_samples = len(pivot)
outliers_fraction = 0.02
#print n_samples
n_outliers = 3
n_inliers = n_samples - n_outliers
pivot = pivot.fillna(0)
ecliptic_fit_android = EllipticEnvelope(contamination=outliers_fraction).fit(pivot)


