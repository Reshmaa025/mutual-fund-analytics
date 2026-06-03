import pandas as pd
import requests

scheme_code = "125497"

url = f"https://api.mfapi.in/mf/{scheme_code}"

response = requests.get(url)
data = response.json()

df = pd.DataFrame(data["data"])

df.to_csv("hdfc_top100_live.csv", index=False)

print("NAV data saved successfully!")
print(df.head())