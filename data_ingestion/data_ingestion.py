import pandas as pd
import os

data_path = "data/raw"

csv_files = [f for f in os.listdir(data_path) if f.endswith(".csv")]

print("CSV Files Found:", csv_files)
print("Total Files:", len(csv_files))

for file in csv_files:
    df = pd.read_csv(os.path.join(data_path, file))

    print(f"\nDataset: {file}")
    print("Shape:", df.shape)

    print("\nData Types:")
    print(df.dtypes)

    print("\nFirst 5 Rows:")
    print(df.head())