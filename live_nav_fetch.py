import requests
import pandas as pd
import os

schemes = {
    "SBI Bluechip": 119551,
    "ICICI Bluechip": 120503,
    "Nippon Large Cap": 118632,
    "Axis Bluechip": 119092,
    "Kotak Bluechip": 120841
}

all_data = []

for name, code in schemes.items():
    url = f"https://api.mfapi.in/mf/{code}"
    res = requests.get(url).json()
    
    df = pd.DataFrame(res['data'])
    df['scheme_name'] = name
    df['scheme_code'] = code
    
    all_data.append(df)

final_df = pd.concat(all_data)

# ✅ SAVE FILE (IMPORTANT PART)
output_path = "data/raw/multi_scheme_nav.csv"
final_df.to_csv(output_path, index=False)

print("Saved at:", output_path)
print(final_df.head())