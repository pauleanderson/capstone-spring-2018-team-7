from pymongo import MongoClient
import pandas as pd
import sys

## connect to the database
client = MongoClient ('localhost', 27017)
data = client.apps

## start with Android data
android = data.android
df = pd.DataFrame(list(android.find({"country":"au"})))
non_pbm_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
#print(df.loc[1:6, :])

#Find all the appId duplicates copy into a new dataframe and sort
new_df = pd.concat(g for _, g in df.groupby("appId") if len(g) > 1)
#print(new_df.to_string().translate(non_pbm_map))

#Inner join
df_sliced = new_df[["appId", "country", "rank", "date"]].copy()
left_df = new_df.drop_duplicates(subset="appId", keep = "first")
right_df = df_sliced.subtract(left_df)



merged_df = left_df.merge(right_df, on="appId", validate="one_to_many")
print(merged_df.to_string().translate(non_pbm_map))


