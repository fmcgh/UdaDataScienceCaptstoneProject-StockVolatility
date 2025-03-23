stock_symbol = "PLTR"
start_date = "2021-01-01"
end_date = "2025-03-21"

# Model parameters
garch_order = (1, 1)
rolling_window = 20

# Value at Risk (VaR) confidence levels
var_confidence_levels = [0.95, 0.99]

# Output settings
save_plots = True
output_dir = "Outputs/"
