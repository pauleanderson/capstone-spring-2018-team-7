from pymongo import MongoClient
import pandas as pd
import sys

## working code
client = MongoClient ('localhost', 27017)
data = client.apps

android = data.android
df = pd.DataFrame(list(android.find({"country":"au"})))
non_pbm_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
#print(df.loc[1:6, :])

new_df = pd.concat(g for _, g in df.groupby("appId") if len(g) > 1)
print(new_df.to_string().translate(non_pbm_map))



