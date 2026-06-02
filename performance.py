import pandas as pd

df = pd.read_csv("data/raw/all_mutual_funds.csv")

df["date"] = pd.to_datetime(df["date"])
df = df.sort_values(["fund_name", "date"])

df["daily_return"] = df.groupby("fund_name")["nav"].pct_change()
returns = df.groupby("fund_name")["daily_return"].mean() * 100

print("\nAverage Daily Returns (%)")
print(returns.sort_values(ascending=False))
best_fund = returns.idxmax()
print("\nBest Performing Fund:", best_fund)
risk = df.groupby("fund_name")["daily_return"].std() * 100

print("\nRisk (Volatility %)")
print(risk.sort_values(ascending=False))