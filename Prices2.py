import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from plotly.offline import iplot
import datetime

# read the csv files of 4 different companies
df = pd.read_csv('/Users/admin/Desktop/DS_Projects/individual_stocks_5yr/SCHW_data.csv')
# path = pd.read_csv('/Users/admin/Desktop/DS_Projects/individual_stocks_5yr/TXN_data.csv')
# path = pd.read_csv('/Users/admin/Desktop/DS_Projects/individual_stocks_5yr/WFC_data.csv')
# path = pd.read_csv('/Users/admin/Desktop/DS_Projects/individual_stocks_5yr/XRAY_data.csv')
# df.head()

# analyse the daily price change in stock,
# create a new column called 'Daily_Price_Change'

df['Daily_Price_Change'] = df['close']-df['open']
print(df.head())
# create a new column (feature) showing 1-day percentage change of stock prices
df['1day % return'] = ((df['close']-df['open'])/df['close'])*100
# visualize the 1-day change as the y value
fig=px.line(df, x='date', y='volume', title='Company')
# print(fig.show())


# analyze monthly mean of close feature, resample the data, check the data types
df2 = df.copy()
# print(df2.dtypes)
# since date is an object, we must convert it to a datetime object, set date as index
df2['date'] = pd.to_datetime(df2['date'])
df2.set_index('date', inplace=True)
print(df2.head())


# grab teh data between 2016 and 2018
print(df2['2016-01-04':'2018-02-07'].head())
# access 'close' column and resample data on basis of average monthly ('M') changes
print(df2['close'].resample('M').mean())
print(df2['close'].resample('Y').mean().plot())
plt.show()
# input kind of plot to see the frequency
# resampling generates a unique sampling distribution on basis of actual data,
# in order to visualize frequency(Monthly, Yearly, Weekly, Quarterly)














