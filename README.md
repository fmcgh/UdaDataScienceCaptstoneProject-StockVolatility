# UdaDataScienceCaptstoneProject-StockVolatility
Capstone Project with Udacity for Data Science Nanodegree. Reviewing stock volatility. 

## GitHub Repo Link
https://github.com/fmcgh/UdaDataScienceCaptstoneProject-StockVolatility


## Medium Article Link
You can [view it here!](https://medium.com/@theniallmackenzie/forecasting-stock-volatility-a-glimpse-into-pltrs-future-with-machine-learning-be4f0e636e03)

## Project Report
Please see the Project Report 'CaptstoneProjectForecastingStockVolatilityReport.pdf' in the root directory for this repository.

## Problem Statement

Can we model and forecast volatility for a given stock or index?

### Use case:

In application, this may be used to interpet securities data to predict whether the is impending volatility in the stock.

This can be used as an interest piece on risk appetite and seeing whether this is possible. 

In a more advanced, algo-trading settings, this may act as a component to indicate volatility. 

Importantly, this project is entirely academic and simply a view to the power of Machine Learning in forecasting potential and impending stock volatility. 

While there is no evidence that it can predict the future, backtest outputs are included below to verify its historical accuracy with existing, real world data. 

### Further Context; an extension of prior academic research

In my previous Udacity project, I attempted to see if we could predict whether a stock would be up or down. 

(You can view the [previous project's Medium article here](https://medium.com/@theniallmackenzie/how-i-predicted-the-stock-market-b6e2d96d461e))

Specifically, this used the 'stable' Vanguard Information Technology ETF (VGT) and comparatively volatile BitCoin (BTC).

It was easy to see that on a corrected, percentage based value shift the correlation in movements at a glance.

While the functionality was proved, the accuracy was poor, I had the incling that volatility in this case was a major issue in predicting stock up vs stock down. 

(Not to mention that more advanced predictive modelling methods would likely equally improve the outcome)

In furtherance of this prior project, I am now seeking to better interpret and map volatility estimates for stocks.

### And so:

This program seeks to predict volatiltiy ahead of time, daily and weekly for Palantir Technologies Inc. (PLTR). 

Specifically, we will be applying GARCH models, volatility surfaces, rolling standard deviation, VaR (Value at Risk).

## Project Overview
This project leverages historical stock data from Yahoo Finance to model and forecast the volatility of Palantir Technologies Inc. (PLTR) stock using GARCH models. 

The goal is to quantify recent volatility, identify volatility clusters, forecast future volatility, and estimate Value at Risk (VaR) under various confidence intervals. 

This has been run for two separate time-series: 

- Daily: This would need to be run every day to predict the next days volatility
- Weekly: This would need to be run every week to predict the next weeks volatility

Both perform well, it may be useful to attempt this for the next month also, however as the time series increases the accuracy will decrease. 

How often this is run equally depends on the risk appetite of the user. 

## Dataset Details

- **Source:** Data is obtained using the `data_download.py` script, which retrieves historical PLTR stock data from Yahoo Finance via the yfinance API.

- **Data Fields:** Daily Open, High, Low, Close, Adjusted Close, and Volume.

- **Derived Features:** The data is processed in the `data_pipeline.py` where log returns, rolling standard deviations, and lagged volatility (as volatility proxies) are calculated.

- **Time Period:** January 1, 2021 – March 21, 2025. This is defined in settings and updated with data_download.py. The data is already downloaded in the output folder, if you wish to change the data you will need to update settings.py and redownload via data_download.py.

## Project Results

- **Daily Model:**  

  A *GARCH(1,1) model is applied to daily log returns. The model summary shows a small, non-significant mean return with volatility parameters capturing conditional *heteroskedasticity 
  
  *GARCH, *heteroskedasticity see: 
  - https://www.investopedia.com/terms/h/heteroskedasticity.asp 
  - https://stats.lse.ac.uk/q.yao/qyao.links/paper/ej08.pdf
  - https://www.learnsignal.com/blog/garch-model/  

  **Backtest Results:**  

  - *VaR 95%:* Observed exceedance rate of ~3.5% vs. expected 5% (PASS).  

  - *VaR 99%:* Observed exceedance rate of ~1.14% vs. expected 1% (PASS).

- **Weekly Model:**  
  Daily data is resampled to weekly frequency. The GARCH model on weekly data produces a flatter volatility forecast due to data smoothing from fewer observations.  

  **Backtest Results:**  

  - *VaR 95%:* Observed exceedance rate of ~5% (PASS).  

  - *VaR 99%:* Observed exceedance rate is near 0% (PASS).

You can view the visualisations for both the daily and the weekly models in the /outputs location.

## Setup and Installation
**Clone the Repository:**
   git clone https://github.com/yourusername/PLTR-stock-volatility.git

Navigate to the repository: 
- cd UdaDataScienceCaptstoneProject-StockVolatility

Install Dependencies:

pip install -r requirements.txt

Run the Application:
- cd PLTR-stock-volatility
- python main.py


**Database Setup**

This project does not use a live connection to the yfinance API. Instead, data is managed through CSV files which are already saved to ensure repeatable results:

The data_download.py script uses yfinance to fetch PLTR stock data.

The downloaded data is stored as CSV files in the /Outputs directory.

The data_pipeline.py then loads this data, cleans it, and calculates derived features (log returns and rolling volatility).

This process is critical as it transforms raw stock data into a format suitable for volatility modeling, ensuring that the data used for the GARCH model and VaR estimation accurately reflects historical price dynamics.

*You can change the ingestion data to anything available in Yahoo Finance by adjusting the Symbol, Start and End dates in settings.py and running 'data_download.py' separately to main.py.

**Data Visualisation**
The project generates several visual outputs, saved in the Outputs/ folder:

### Returns Plots
- **returns_plot_daily.png:**  
  - **X-Axis:** Dates (daily observations).  
  - **Y-Axis:** Daily log returns (i.e., the natural log of the ratio of consecutive closing prices).  
  - **What It Tells Us:**  
    This graph shows the day-to-day percentage change in PLTR's stock price. It helps identify periods of high volatility versus periods of relative calm.

- **returns_plot_weekly.png:**  
  - **X-Axis:** Dates (weekly, typically the last trading day of each week).  
  - **Y-Axis:** Weekly log returns (aggregated from daily data).  
  - **What It Tells Us:**  
    This plot smooths out daily fluctuations to show broader trends over the week. It provides insight into longer-term return patterns, which can differ from daily dynamics.

### Volatility Forecast Plots
- **volatility_plot_daily.png:**  
  - **X-Axis:** Dates (daily observations).  
  - **Y-Axis:** Predicted volatility (in percentage).  
  - **Legends:**  
    - **GARCH Volatility:** The volatility forecast from the GARCH(1,1) model.  
    - **Rolling Volatility:** The volatility calculated using a rolling standard deviation of daily log returns.  
  - **What It Tells Us:**  
    This graph compares the model-based volatility forecast with a simple historical measure. It shows how well the GARCH model captures the changes in volatility on a daily basis, highlighting volatility clustering and shifts in market behavior.

- **volatility_plot_weekly.png:**  
  - **X-Axis:** Dates (weekly observations).  
  - **Y-Axis:** Predicted volatility (in percentage).  
  - **Legends:**  
    - **GARCH Volatility:** The forecasted volatility from the GARCH model on weekly data.  
    - **Rolling Volatility:** The rolling volatility computed on the weekly log returns.  
  - **What It Tells Us:**  
    Similar to the daily plot, this graph shows the comparison on a weekly basis. Due to fewer data points and aggregation, the GARCH forecast often appears smoother and less reactive to short-term fluctuations.

### VaR Plots
- **var_plot_daily.png:**  
  - **X-Axis:** Dates (daily observations).  
  - **Y-Axis:** Log returns and VaR thresholds.  
  - **Legends:**  
    - **VaR Curves (e.g., var_95, var_99):** These curves represent the loss thresholds such that only a given percentage (e.g., 5% for var_95 and 1% for var_99) of daily returns are expected to fall below these values.  
    - **Log Returns:** Plotted in grey, showing the actual daily returns.  
  - **What It Tells Us:**  
    This plot overlays the model’s risk thresholds on the actual daily returns. It helps assess how often the returns exceed (are worse than) the predicted risk levels, validating the VaR estimates.

- **var_plot_weekly.png:**  
  - **X-Axis:** Dates (weekly observations).  
  - **Y-Axis:** Weekly log returns and VaR thresholds.  
  - **Legends:**  
    - **VaR Curves (e.g., var_95, var_99):** The risk thresholds for the weekly data.  
    - **Log Returns:** The actual weekly log returns.  
  - **What It Tells Us:**  
    This graph shows the risk evaluation on a weekly level. It indicates how often the weekly returns breach the VaR thresholds, providing an overall view of the risk over a longer time horizon.

While further validation for the model outputs can be performed, for the moment, this backtest outputs referenced above give enough security in the models performance for this project, per: 

  **Backtest Results:**  

- **Daily Model:**

  - *VaR 95%:* Observed exceedance rate of ~3.5% vs. expected 5% (PASS).  

  - *VaR 99%:* Observed exceedance rate of ~1.14% vs. expected 1% (PASS).

- **Weekly Model:**   

  - *VaR 95%:* Observed exceedance rate of ~5% (PASS).  

  - *VaR 99%:* Observed exceedance rate is near 0% (PASS).

These results can also be viewed via backtest_runner() when running main.py for the models.


**How It Works**
Data Collection:
Historical PLTR stock data is downloaded using yfinance in data_download.py.

**Preprocessing:**
The raw data is loaded and transformed in data_pipeline.py to compute log returns and rolling volatility.

**Modeling:**
A GARCH(1,1) model is fitted to both daily and weekly data to capture conditional heteroskedasticity and forecast volatility.

Why GARCH(1,1)?
The GARCH(1,1) model is chosen for its simplicity and robustness. 

It effectively captures volatility clustering—a common phenomenon in financial time series—without overfitting. 

While more complex models can be applied GARCH(1,1) strikes a good balance between performance and interpretability, making it a standard benchmark for volatility forecasting.

**Risk Evaluation:**
The model outputs are used to calculate Value at Risk (VaR), which is then backtested against actual returns.


**Contribution**
This project was completed as part of an academic course and there is no intention to update.

You are free to use any of the content from this Repository that may be useful, or build on it as you please.

There is no intention to include any contributions to this project.

**Licence**
This project is licensed under the MIT License.

This project and it's application is purely academic and has been produced as part of an academic study with Udacity.