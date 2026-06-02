import pandas as pd

df = pd.read_csv("data/raw/all_mutual_funds.csv")

print(df.head())
print(df.shape)
print(df.columns)
print("\nUnique Funds:")
print(df["fund_name"].unique())

print("\nFund count:")
print(df["fund_name"].value_counts())
print("\nDate range:")
print(df["date"].min(), "to", df["date"].max())

print("\nNAV stats:")
print(df["nav"].describe())
print("\nMissing values:")
print(df.isnull().sum())