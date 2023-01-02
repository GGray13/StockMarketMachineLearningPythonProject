import pandas as pd


# Define data range
start_date = '2010-01-01'
end_date = '2010-12-31'
dates = pd.date_range(start_date, end_date)

# Create empty dataframe
df1 = pd.DataFrame(index=dates)

# Read SPY data into temporary dataframe
dfSPY = pd.read_csv("Data/SPY.csv", index_col="Date",
                    parse_dates=True, usecols=['Date', 'Adj Close'],
                    na_values=['nan'])

dfSPY = dfSPY.rename(columns={'Adj Close': 'SPY'})

df1 = df1.join(dfSPY, how='inner')
df1 = df1.dropna()

symbols = ['GOOG', 'IBM', 'GLD']
for symbol in symbols:
    df_temp = pd.read_csv("Data/{}.csv".format(symbol), index_col='Date',
                          parse_dates=True, usecols=['Date', 'Adj Close'],
                          na_values=['nan'])
    df_temp = df_temp.rename(columns={'Adj Close': symbol})
    df1 = df1.join(df_temp)
print(df1)