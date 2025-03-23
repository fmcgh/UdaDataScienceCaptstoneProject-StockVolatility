from data_pipeline import (
    calculate_log_returns,
    calculate_rolling_volatility,
    load_data,
    save_transformed_data,
)
from model import calculate_var, fit_garch_model
from settings import garch_order, rolling_window
from utils import plot_returns, plot_var, plot_volatility
from tests.backtest import backtest_runner

def run_pipeline(data, label):
    """
    Run the volatility modeling pipeline.

    Execution Flow:
      1. Compute log returns and plot them.
      2. Calculate rolling volatility and save transformed data.
      3. Fit a GARCH model.
      4. Plot volatility forecast and compute VaR.
      5. Plot VaR and print model summary.

    Input:
        data (DataFrame): Stock data.
        label (str): Frequency label 'daily'/'weekly'

    Output:
        None. Prints model summary and saves plots/data.
    """
    data = calculate_log_returns(data)
    plot_returns(data, label)
    data = calculate_rolling_volatility(data, rolling_window)
    save_transformed_data(data)
    fitted_model = fit_garch_model(data, garch_order)
    plot_volatility(data, fitted_model, label)
    var_df = calculate_var(fitted_model)
    plot_var(data, var_df, label)
    print(f"{label.capitalize()} model summary:")
    print(fitted_model.summary())


def main():
    """
    Execute the daily and weekly volatility modeling pipelines.

    Execution Flow:
      1. Load raw daily stock data.
      2. Run the daily pipeline.
      3. Resample data to weekly and run the weekly pipeline.
      4. Run the backtest to confirm accuracy

    Input:
        None

    Output:
        None.
    """
    daily_data = load_data()
    run_pipeline(daily_data, label="daily")

    weekly_data = daily_data.resample("W-FRI").last()
    run_pipeline(weekly_data, label="weekly")

    backtest_runner()


if __name__ == "__main__":
    # main()
    backtest_runner(tolerance=0.05)
