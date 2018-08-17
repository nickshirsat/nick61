 import pandas as pd
 ds=pd.read_csv('Game_medal.csv', encoding="ISO-8859-1")
 ds.head()
 ds.tail(10)
 ds.describe()
 ds.shape
 ds.shift
 ds.info
 ds.NOC
 ds.plot()
 import matplotlib.pyplot as plt
 plt.plot(ds.Edition)
 plt.plot(ds.Edition, label="Year Of Events")
 plt.plot(ds.Edition, color="Red", label="Year Of Events")