import pandas as pd

def get_max_close(symbol):
    """Return the max closing value for stock indicated by symbol.

    Note: Data for a stock is stored in file data/<symbol>.csv
    """
    df = pd.read_csv("Data/{}.csv".format(symbol))  # read in data
    return df['Close'].max()  # compute and return max

def test_run():
    """Function called by test run."""
    for symbol in ['AAPL', 'IBM']:
        print("Max close")
        print(symbol, get_max_close(symbol))


if __name__ == "__main__":
    test_run()