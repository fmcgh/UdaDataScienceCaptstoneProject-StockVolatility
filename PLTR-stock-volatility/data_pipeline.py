import os
from datetime import datetime

import numpy as np
import pandas as pd
from settings import end_date, output_dir, start_date, stock_symbol


def load_data():
    """
    Load stock data from CSV saved from Yahoo Finance.

    Input:
        None (uses settings)

    Output:
        DataFrame: Stock data with a Date index.
    """
    file_path = os.path.join(
        output_dir, f"{stock_symbol}_raw_{start_date}_to_{end_date}.csv"
    )
    if not os.path.exists(file_path):
        raise FileNotFoundError(
            f"Data file not found: {file_path}. Please run data_download.py."
        )
    data = pd.read_csv(file_path, index_col="Date", parse_dates=True)
    return data


def calculate_log_returns(data):
    """
    Compute log returns from close prices.

    Input:
        data (DataFrame): Contains 'Close' column.

    Output:
        DataFrame: Data with added 'log_returns' column.
    """
    data["log_returns"] = np.log(data["Close"] / data["Close"].shift(1))
    data.dropna(inplace=True)
    return data


def calculate_rolling_volatility(data, window):
    """
    Calculate rolling standard deviation as volatility proxy.

    Input:
        data (DataFrame): Contains 'log_returns'.
        window (int): Rolling window size.

    Output:
        DataFrame: Data with added 'rolling_volatility' column.
    """
    data["rolling_volatility"] = (
        data["log_returns"].rolling(window=window).std()
    )
    return data


def save_transformed_data(data):
    """
    Save transformed data (returns and volatility) to CSV.

    Input:
        data (DataFrame): Transformed stock data.

    Output:
        CSV file saved in output_dir.
    """
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    file_path = os.path.join(
        output_dir, f"transformed_data_{stock_symbol}_{timestamp}.csv"
    )
    data.to_csv(file_path)
    print(f"Transformed data saved to {file_path}")
