import pandas as pd

df = pd.read_csv("data/rawdata.csv")

# Drop useless column
if "Timestamp" in df.columns:
    df = df.drop(columns=["Timestamp"])

# Rename columns (simple names)
df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

# Remove duplicates & missing
df = df.drop_duplicates()
df = df.dropna()

# Save cleaned data
df.to_csv("data/cleaned_data.csv", index=False)

print("Cleaned data saved ")