import pandas as pd
import plotly.express as px

df = pd.read_csv("data/raw/all_mutual_funds.csv")
df["date"] = pd.to_datetime(df["date"])

# ---- NAV Trend Chart ----
fig1 = px.line(
    df,
    x="date",
    y="nav",
    color="fund_name",
    title="Mutual Fund NAV Trends"
)

fig1.show()

# ---- Latest NAV Comparison ----
latest = df.sort_values("date").groupby("fund_name").tail(1)

fig2 = px.bar(
    latest,
    x="fund_name",
    y="nav",
    title="Latest NAV Comparison",
    color="fund_name"
)

fig2.show()