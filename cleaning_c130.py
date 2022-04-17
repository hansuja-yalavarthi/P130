import pandas as pd 
import csv
df= pd.read_csv("data_merged_p129.csv")
print(df.shape)
del df["Star_name"]
del df["Mass"]
del df["Radius"]
del df["Distance"]
print(list(df))
print(df.shape)
df=df.rename({
    'Star Name':'star_name',
   'Distance.1' :'planet_discovery_method',
   'Mass.1': 'mass',
   'Radius.1': 'radius',
},axis='columns')
print(list(df))
print(df.shape)
df.to_csv('data_from_p130.csv')