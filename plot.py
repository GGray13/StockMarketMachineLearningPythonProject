import pandas as pd
import matplotlib.pyplot as plt


def get_plot():
    df = pd.read_csv("Data/AAPL.csv")
    df[['Close', 'Adj Close']].plot()  # must be called to show plots
    plt.show()


if __name__ == "__main__":
    get_plot()
