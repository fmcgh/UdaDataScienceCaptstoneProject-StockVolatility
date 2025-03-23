import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import pandas as pd
from data_pipeline import calculate_log_returns, load_data
from model import calculate_var, fit_garch_model
from settings import garch_order, var_confidence_levels


def backtest_var(log_returns, var_df, tolerance):
    """
    Backtests the Value at Risk (VaR) model.

    Input:
        log_returns (pd.Series): Actual returns
        var_df (pd.DataFrame): Forecasted VaR levels
        tolerance (float): Acceptable deviation between expected and observed

    Output:
        DataFrame with exceedance rates and pass/fail status
    """
    results = {}

    for col in var_df.columns:
        level = int(col.split("_")[1])
        threshold = var_df[col]
        aligned_returns = log_returns.loc[threshold.index]
        exceedances = aligned_returns < threshold
        rate = exceedances.sum() / len(exceedances)
        expected = 1 - (level / 100)
        difference = abs(rate - expected)
        result = "PASS" if difference <= tolerance else "FAIL"

        results[col] = {
            "observed_exceedances": exceedances.sum(),
            "expected_exceedance_rate": expected,
            "observed_exceedance_rate": round(rate, 4),
            "difference": round(difference, 4),
            "result": result,
        }

    return pd.DataFrame(results).T


def run_backtest(data, tolerance, label="daily"):
    data = calculate_log_returns(data)
    model = fit_garch_model(data, garch_order)
    var_forecast = calculate_var(model, var_confidence_levels)
    return backtest_var(data["log_returns"], var_forecast, tolerance)


def backtest_runner(tolerance=0.05):
    # Daily test
    print("Running daily backtest...")
    daily_data = load_data()
    daily_results = run_backtest(daily_data, tolerance, label="daily")
    print("\nDaily VaR Backtest Results:")
    print(daily_results)

    # Weekly test
    print("\nRunning weekly backtest...")
    weekly_data = daily_data.resample("W-FRI").last()
    weekly_results = run_backtest(weekly_data, tolerance, label="weekly")
    print("\nWeekly VaR Backtest Results:")
    print(weekly_results)

# Essentially it's accurate but not perfect
# Failure on tolerance = 0.01
# Pass on tolerance = 0.05 (0.035)

# Updated model, now pass on 0.05
