#!/usr/bin/env python
# This is a shebang line to specify the interpreter what language to use.




# FAANG stock data plotting script.
import yfinance as yf

# Date and time handling.
import datetime as dt

# Data frames.
import pandas as pd

# Plotting.
import matplotlib.pyplot as plt

# Listing files in a folder.
import os

def plot_data():
    """
    Reads the latest CSV file from the data folder, plots the Close prices 
    for all five stocks on a single figure, adds labels and a title, and 
    saves the plot as a timestamped PNG file in the plots folder.
    """

    # Get current date and time.
    now = dt.datetime.now()

    # List all files in the data folder.
    data_files = os.listdir('data/')

    # Sort files
    sorted_data_files = sorted(data_files, reverse=True)

    # Read the most recent file.
    df = pd.read_csv('data/' + sorted_data_files[0], header=[0,1], index_col=0, parse_dates=True)

    # Plot new figure and axis.
    fig, ax = plt.subplots()

    # Plot five stocks
    df['Close'].plot(ax=ax)

    # Titles and axes
    ax.set_xlabel("Date")
    ax.set_ylabel("Closing Price (USD)")
    ax.legend(title="Ticker")
    ax.set_title(df.index[-1].strftime("%Y-%m-%d"))

    file_name = now.strftime("%Y%m%d-%H%M%S") + ".png"
    plt.savefig("plots/" + file_name)
    plt.close()


# Adding this to ensure the function runs when the script is executed directly.
if __name__ == "__main__":
    plot_data()