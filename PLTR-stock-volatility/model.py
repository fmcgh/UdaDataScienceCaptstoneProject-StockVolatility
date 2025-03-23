import numpy as np
import pandas as pd
from arch import arch_model
from settings import var_confidence_levels


def fit_garch_model(data, order=(1, 1)):
    """
    Fits a GARCH model to the stock log returns.

    Input:
        data (pd.DataFrame): DataFrame with 'log_returns'
        order (tuple): GARCH(p, q) model order

    Output:
        Fitted GARCH model object
    """
    model = arch_model(
        data["log_returns"] * 100, vol="GARCH", p=order[0], q=order[1]
    )
    fitted_model = model.fit(disp="off")
    return fitted_model


def calculate_var(fitted_model, confidence_levels=var_confidence_levels):
    """
    Calculates Value at Risk (VaR) based on GARCH volatility forecasts.

    Input:
        fitted_model: GARCH model object after fitting
        confidence_levels (list): List of confidence levels for VaR

    Output:
        DataFrame of VaR forecasts indexed by date
    """
    forecast_vol = fitted_model.conditional_volatility / 100
    var_df = pd.DataFrame(index=fitted_model.conditional_volatility.index)

    for cl in confidence_levels:
        z_score = abs(
            np.percentile(np.random.normal(0, 1, 100000), (1 - cl) * 100)
        )
        var_df[f"var_{int(cl * 100)}"] = -z_score * forecast_vol

    return var_df
