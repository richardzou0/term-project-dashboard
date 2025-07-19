import pandas as pd

# Load the already cleaned CSV
df = pd.read_csv("data.csv")
df.columns = df.columns.str.strip()  # remove trailing spaces just in case

# Ensure numeric and filter 2023 only
df["Value (%)"] = pd.to_numeric(df["Value (%)"], errors="coerce") * 10
df_clean = df[df["Year"] == 2023].dropna(subset=["Value (%)"])

# Save the cleaned data
df_clean.to_csv("data.csv", index=False)

print("✅ Cleaned 2023 data saved to data.csv")
