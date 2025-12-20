# FAANG Stock Data Analysis

This repository contains a small Python project that downloads FAANG stock data, plots closing prices, and automates the process using GitHub Actions.

## Problem 1: Downloading Data

A function downloads the last 5 days of hourly stock price data for FAANG companies:

- META
- AAPL
- AMZN
- NFLX
- GOOG

The data is downloaded using the `yfinance` library and saved as a CSV file in the `data/` folder.  
Each file is named using the current date and time to ensure uniqueness.


## Problem 2: Plotting Data

Another function:

- Opens the most recent CSV file from the `data/` folder
- Plots the **Close prices** for all five stocks on a single chart
- Adds axis labels, a legend, and a title
- Saves the plot as a PNG file in the `plots/` folder using a timestamped filename

This ensures that each run produces a new plot without overwriting previous ones.


## Problem 3: Python Script (`faang.py`)

All functions are combined into a single script called `faang.py`, located in the root of the repository.

Key features:
- Includes a shebang line so it can be run as a script
- Uses an `if __name__ == "__main__":` block so the script runs when executed
- When run, it downloads data and creates a plot automatically

Example command:
```bash
python faang.py


## Problem 4: Automation with GitHub Actions

In this task, GitHub Actions is used to automatically run the FAANG stock script on a schedule.

A workflow file called `github-actions-demo.yml` was created in the `.github/workflows/` folder. This workflow runs the `faang.py` script and saves newly generated plots back to the repository.

### Workflow Triggers

```yaml
on:
  workflow_dispatch:
  schedule:
    - cron: '0 8 * * SAT'
