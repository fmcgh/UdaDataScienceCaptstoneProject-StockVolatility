import os

import matplotlib.pyplot as plt
from settings import output_dir, save_plots, stock_symbol


def plot_returns(data, label):
    """
    Plot stock log returns.

    Input:
        data (DataFrame): 'log_returns'.
        label (str): Frequency label 'daily'/'weekly

    Output:
        Displays and saves the log returns plot.
    """
    plt.figure(figsize=(12, 6))
    data["log_returns"].plot()
    plt.title(f"{stock_symbol} {label.capitalize()} Log Returns")
    plt.xlabel("Date")
    plt.ylabel("Log Returns")
    if save_plots:
        plt.savefig(os.path.join(output_dir, f"returns_plot_{label}.png"))
    plt.show()


def plot_volatility(data, fitted_model, label):
    """
    Plot GARCH and rolling volatility.

    Input:
        data (DataFrame): 'rolling_volatility'.
        fitted_model: GARCH model with 'conditional_volatility'.
        label (str): Frequency label 'daily'/'weekly

    Output:
        Displays and saves the volatility plot.
    """
    plt.figure(figsize=(12, 6))
    plt.plot(
        data.index[-len(fitted_model.conditional_volatility) :],
        fitted_model.conditional_volatility,
        label="GARCH Volatility",
    )
    if "rolling_volatility" in data.columns:
        plt.plot(
            data.index[-len(fitted_model.conditional_volatility) :],
            data["rolling_volatility"][
                -len(fitted_model.conditional_volatility) :
            ]
            * 100,
            label="Rolling Volatility",
        )
    plt.title(f"{stock_symbol} {label.capitalize()} Volatility Forecast")
    plt.xlabel("Date")
    plt.ylabel("Predicted Volatility (%)")
    plt.legend()
    if save_plots:
        plt.savefig(os.path.join(output_dir, f"volatility_plot_{label}.png"))
    plt.show()


def plot_var(data, var_df, label):
    """
    Plot VaR forecasts vs. log returns.

    Input:
        data (DataFrame): Contains 'log_returns'.
        var_df (DataFrame): Contains VaR forecasts.
        label (str): Frequency label 'daily'/'weekly

    Output:
        Displays and saves the VaR plot.
    """
    plt.figure(figsize=(12, 6))
    for col in var_df.columns:
        plt.plot(var_df.index, var_df[col], label=col)
    plt.plot(data["log_returns"], color="grey", alpha=0.3, label="Log Returns")
    plt.title(f"{stock_symbol} {label.capitalize()} Value at Risk (VaR)")
    plt.xlabel("Date")
    plt.ylabel("VaR and Log Returns")
    plt.legend()
    if save_plots:
        plt.savefig(os.path.join(output_dir, f"var_plot_{label}.png"))
    plt.show()
