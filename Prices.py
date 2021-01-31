import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from plotly.offline import iplot
import datetime

# read the csv files of 4 different companies
route = '/Users/admin/Desktop/DS_Projects/individual_stocks_5yr'
companies = ['SCHW_data.csv', 'TXN_data.csv', 'WFC_data.csv', 'XRAY_data.csv']
# _data.csv.columns

# declare a blank dataframe, iterate over companies list, read each csv, specify the path
whole_data = pd.DataFrame()
for file in companies:
    now_df = pd.read_csv(route+'/'+file)
    whole_data = pd.concat([whole_data, now_df])
# now_df is concatted to the empty whole_data dataframe
# check amount of rows and columns, and head
print(whole_data.shape)
print(whole_data.head())


# create new list, iterate over list, call each different stock name
stocks = whole_data['Name'].unique()
# Enumerate() method adds a counter to an iterable and returns it in a form of enumerate object.
# This enumerate object can then be used directly in for loops,
# or be converted into a list of tuples using list() method.
# call enum over list to plot the closing price of each stock on a single figure,
# index starts with 1, i will contain index, 2x2 matrix, every stock goes through i
# Convert date into datetime

whole_data['date']=pd.to_datetime(whole_data['date'])

# to check the datatypes, whole_data.dtypes

plt.figure(figsize=(20, 12))
for i, company in enumerate(stocks, 1):
    plt.subplot(2, 2, i)
    df = whole_data[whole_data['Name'] == company]
    plt.plot(df['date'], df['close'])
    plt.title(company)
    plt.xticks(rotation='vertical')
    plt.show()
# 'Name' condition is passed into whole_data df
# 'date' represent x-axis, 'close' represents y=axis, because of the order of parameters for plt.plot











