import os
import yfinance as yf
from settings import end_date, output_dir, start_date, stock_symbol


def download_and_save_data():
    """
    Downloads PLTR stock data from Yahoo Finance for the defined time period
    and saves it as a CSV file.

    Input:
        None (uses config variables from settings.py)

    Output:
        CSV file saved in the outputs/ directory
    """
    data = yf.download(
        stock_symbol,
        start=start_date,
        end=end_date,
        auto_adjust=True,
        multi_level_index=False,
    )

    # Adj Close currently unavailable in the API
    data = data.dropna(subset=["Close"])

    os.makedirs(output_dir, exist_ok=True)

    file_path = (
        f"{output_dir}{stock_symbol}_raw_{start_date}_to_{end_date}.csv"
    )
    data.to_csv(file_path)
    print(f"Saved to {file_path}")


if __name__ == "__main__":
    download_and_save_data()
