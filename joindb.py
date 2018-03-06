from pymongo import MongoClient
import pandas as pd
import sys

## working code
client = MongoClient ('localhost', 27017)
data = client.apps

apple = data.apple
df = pd.DataFrame(list(apple.find()))
non_pbm_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
print(df.to_string().translate(non_pbm_map))
