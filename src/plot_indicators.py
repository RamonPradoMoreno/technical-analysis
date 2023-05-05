from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

stock_name = "TSLA"


stock_analysis_result = Path(f"./results/{stock_name}.csv")
# Load data
df = pd.read_csv(stock_analysis_result, sep=",")

print(df.head())

plt.plot(df.trend_macd, label="MACD")
plt.plot(df.trend_macd_signal, label="MACD Signal")
plt.plot(df.trend_macd_diff, label="MACD Difference")
plt.title("MACD, MACD Signal and MACD Difference")
plt.legend()
plt.show()
