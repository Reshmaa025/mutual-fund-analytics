import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/raw/all_mutual_funds.csv")

df["date"] = pd.to_datetime(df["date"])
hdfc = df[df["fund_name"] == "HDFC_Top100"]

plt.figure()
plt.plot(hdfc["date"], hdfc["nav"])
plt.title("HDFC Top 100 NAV Trend")
plt.xlabel("Date")
plt.ylabel("NAV")
plt.show()
sbi = df[df["fund_name"] == "SBI_Bluechip"]

plt.figure()
plt.plot(hdfc["date"], hdfc["nav"], label="HDFC")
plt.plot(sbi["date"], sbi["nav"], label="SBI")

plt.legend()
plt.title("Fund Comparison")
plt.xlabel("Date")
plt.ylabel("NAV")
plt.show()