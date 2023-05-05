from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.dates import AutoDateFormatter, AutoDateLocator

# from matplotlib.widgets import Cursor
import mplcursors as mpc

plt.style.use("bmh")
stock_name = "SPY"


stock_analysis_result = Path(f"./results/{stock_name}.csv")
# Load data
df = pd.read_csv(stock_analysis_result, sep=",")


date_in_datetime = pd.to_datetime(df.Date)
df.Date = date_in_datetime
# Create the plot
fig, ax = plt.subplots(2, sharex=True)


# X-axis plot 1
plt.setp(ax[0].get_xticklabels(), rotation=30, ha="right")
ax[0].xaxis.set_major_locator(AutoDateLocator())
ax[0].xaxis.set_major_formatter(AutoDateFormatter("%y-%m-%d"))
ax[0].set_xlim(df["Date"].values[0], df["Date"].values[-1])

# X-axis plot 2
plt.setp(ax[1].get_xticklabels(), rotation=30, ha="right")
ax[1].xaxis.set_major_locator(AutoDateLocator())
ax[1].xaxis.set_major_formatter(AutoDateFormatter("%y-%m-%d"))
ax[1].set_xlim(df["Date"].values[0], df["Date"].values[-1])

# Y-axis plot 1
ax[0].plot(df["Date"], df["Close"], label="close price")
# Y-axis plot 2
ax[1].plot(df["Date"], df["trend_macd"], label="MACD")
ax[1].plot(df["Date"], df["trend_macd_signal"], label="MACD Signal")
ax[1].plot(df["Date"], df["trend_macd_diff"], label="MACD Difference")

# Labels plot 1
ax[0].set_title(r"Closing Price")
ax[0].set_xlabel("Date")
ax[0].set_ylabel("Closing Price")
ax[0].legend(loc="best", framealpha=0.5)

# Labels plot 2
ax[1].set_title(r"MACD Analysis")
ax[1].set_xlabel("Date")
ax[1].set_ylabel("MACD Analysis")
ax[1].legend(loc="best", framealpha=0.5)


# Use tight layout
fig.tight_layout()
mpc.cursor(hover=True)
plt.show()

# plt.plot(df.trend_macd, label="MACD")
# plt.plot(df.trend_macd_signal, label="MACD Signal")
# plt.plot(df.trend_macd_diff, label="MACD Difference")
# plt.title("MACD, MACD Signal and MACD Difference")
# plt.legend()
# plt.show()
