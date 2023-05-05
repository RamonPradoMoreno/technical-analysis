"""
Calculates all indicators for a given time series CSV.
"""
from pathlib import Path

import pandas as pd
import ta

stock_name = "SPY"

stock_timeseries_file = Path(f"./historical_data/{stock_name}.csv")
stock_analysis_result = Path(f"./results/{stock_name}.csv")
# Load data
df = pd.read_csv(stock_timeseries_file, sep=",")

# Clean nan values
df = ta.utils.dropna(df)

print(df.columns)

# Add all ta features filling nans values
df = ta.add_all_ta_features(df, "Open", "High", "Low", "Close", "Volume", fillna=True)

# Save a new file that includes the ta features
df.to_csv(stock_analysis_result)
