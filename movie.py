import pandas as pd
ds=pd.read_csv('movie_metadata.csv',encoding="ISO-8859-1")
ds.head()
ds.shape
ds.info()
ds.imdb_score.describe()
ds['movie_title']   # display movie_title column
ds['duration'][:10]  # First 10 records of duration column
ds[['budget','gross']] # select multiple columns
ds[ds1['duration'] > 120] # select movie more than 2 hr duration