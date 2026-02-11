import pandas as pd

# Load data
df = pd.read_csv(
    "data/HHS_Unaccompanied_Alien_Children_Program.csv"
)

# Date parsing
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

# Clean HHS Care column
df["Children in HHS Care"] = (
    df["Children in HHS Care"]
    .astype(str)
    .str.replace(",", "")
    .astype(float)
)

# Drop invalid dates
df = df.dropna(subset=["Date"])

# Sort and index
df = df.sort_values("Date").set_index("Date")

# Derived metrics
df["Total System Load"] = (
    df["Children in CBP custody"] +
    df["Children in HHS Care"]
)

df["Net Intake"] = (
    df["Children transferred out of CBP custody"] -
    df["Children discharged from HHS Care"]
)

print(df.head())
