from pymongo import MongoClient
import pandas as pd
import sys

## working code
client = MongoClient ('localhost', 27017)
data = client.apps

android = data.android
df = pd.DataFrame(list(android.find()))
non_pbm_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
#print(df.loc[1:6, :])

ids = df["_id"]
new_df = df[ids.isin(ids[ids.duplicated()])]
print(new_df.to_string().translate(non_pbm_map))
print(ids.to_string().translate(non_pbm_map))

