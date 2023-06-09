import datetime as dt
import matplotlib.pyplot as plt
from  matplotlib import style
import pandas as pd
import pandas_datareader.data as web

style.use("ggplot")


#####Retrieving data
#start = dt.datetime(2000,1,1)
#end = dt.datetime(2016,12,31)

#df = web.DataReader('TSLA', 'stooq',start, end)

#print(df.head())

#df.to_csv('tsla.csv')


##We want our indexes to be dates
df = pd.read_csv("tsla.csv",parse_dates=True,index_col=0)
#print(df.head())
df[["Open","Close"]].plot()

plt.show()

