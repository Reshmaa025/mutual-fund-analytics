import requests
import pandas as pd

funds = {
    "HDFC_Top100": 125497,
    "SBI_Bluechip": 119551,
    "ICICI_Bluechip": 120503,
    "Nippon_LargeCap": 118632,
    "Axis_Bluechip": 119092,
    "Kotak_Bluechip": 120841
}

all_data = []

for name, code in funds.items():
    url = f"https://api.mfapi.in/mf/{code}"
    response = requests.get(url)
    data = response.json()

    df = pd.DataFrame(data["data"])

    df["date"] = pd.to_datetime(df["date"], format="%d-%m-%Y")
    df["nav"] = df["nav"].astype(float)

    df["fund_name"] = name

    all_data.append(df)

# combine all funds
final_df = pd.concat(all_data, ignore_index=True)

print(final_df.head())
print(final_df.shape)
print(final_df.dtypes)

# save file
final_df.to_csv("data/raw/all_mutual_funds.csv", index=False)