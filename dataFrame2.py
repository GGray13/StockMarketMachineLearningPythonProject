import pandas as pd
import matplotlib as plt
import os


def symbol_to_path(symbol, base_dir="Data"):
    return os.path.join(base_dir, ".csv".format(str(symbol)))


def get_data(symbols, dates):
    df = pd.DataFrame(index=dates)
    if 'SPY' not in symbols:
        symbols.insert(0, 'SPY')


for symbol in symbols:
    df_temp = pd.read_csv(symbol_to_path(symbol), index_col='Date',
                          parse_dates=True, usecols=['Date', 'Adj Close'],
                          na_values=['nan'])
    df_temp = df_temp.rename(columns={'Adj Close': symbol})
    df = df.join(df_temp)
    if symbol == 'SPY':
        df = df.dropna(subset=["SPY"])

    return df

def plot_data(df):
    df.plot()
    plt.show()