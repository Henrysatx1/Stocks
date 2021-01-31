# Analyze whether stock prices of these tech companies are correlated or not?
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from plotly.offline import iplot
import datetime

SCHW = pd.read_csv('/Users/admin/Desktop/DS_Projects/individual_stocks_5yr/SCHW_data.csv')
TXN = pd.read_csv('/Users/admin/Desktop/DS_Projects/individual_stocks_5yr/TXN_data.csv')
WFC = pd.read_csv('/Users/admin/Desktop/DS_Projects/individual_stocks_5yr/WFC_data.csv')
XRAY = pd.read_csv('/Users/admin/Desktop/DS_Projects/individual_stocks_5yr/XRAY_data.csv')

# grab the close column from each df
# create a blank dataframe called 'close'

closing = pd.DataFrame()
# assign features at closing price for the four companies
closing['SCHW'] = SCHW['close']
closing['TXN'] = TXN['close']
closing['WFC'] = WFC['close']
closing['XRAY'] = XRAY['close']
# print(closing.head())

sns.pairplot(data=closing)
plt.show()
# see 4X4 matrix since there are 4 columns with a linear relationship
# visualize a heatmap that shows the correlation of stock prices of 'close' df
sns.heatmap(data=closing.corr(), annot=True)
plt.show()



# Analyze Daily returns of each stock and how they are correlated
# define a blank dataframe called 'Daily'
daily = pd.DataFrame()
# analyze the stock price change for SCWHAB, WFC, XRAY, TXN and create a new feature for it
daily['SCHW_change'] = ((SCHW['close']-SCHW['open'])/SCHW['close']) * 100
daily['WFC_change'] = ((WFC['close']-WFC['open'])/WFC['close']) * 100
daily['XRAY_change'] = ((XRAY['close']-XRAY['open'])/XRAY['close']) * 100
daily['TXN_change'] = ((TXN['close']-TXN['open'])/TXN['close']) * 100
print(daily.head())
# stock prices show in terms of percentage
# to see in a piarplot and matrix
sns.pairplot(data=daily)
#plt.show()
sns.heatmap(data=daily.corr(), annot=True)
#plt.show()
# if there is a high change in '' stock, there is a % of high change in '' stock





# Analyze the value at risk for tech companies
# call a dristribution plot, check standard deviation
sns.distplot(daily['SCHW_change'])
print(daily['SCHW_change'].std())
# std shows how much each score lies from the mean
# 1 = 68% of entire data,
# there is a 68% change the daily return will lie in range of '' & ''
