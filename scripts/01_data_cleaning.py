import pandas as pd
import os

# --------------------------------------------------
# 1. FILE PATH
# --------------------------------------------------

file_path = r"C:\Users\Sathya\ETF_dataset\ETF_monthly_adjusted_close.csv"

# --------------------------------------------------
# 2. LOAD DATA
# --------------------------------------------------

df = pd.read_csv(file_path)

print("=" * 70)
print("INITIAL DATASET")
print("=" * 70)

print("\nShape:")
print(df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nFirst 5 rows:")
print(df.head())

print("\nLast 5 rows:")
print(df.tail())


# --------------------------------------------------
# 3. CONVERT DATE COLUMN
# --------------------------------------------------

df["Date"] = pd.to_datetime(df["Date"])

# Sort chronologically
df = df.sort_values("Date")

# Remove duplicate dates
df = df.drop_duplicates(subset="Date")


# --------------------------------------------------
# 4. KEEP ONLY OUR 9 ETFs
# --------------------------------------------------

etfs = [
    "NIFTYBEES",
    "BANKBEES",
    "JUNIORBEES",
    "ITBEES",
    "PHARMABEES",
    "AUTOBEES",
    "INFRABEES",
    "GOLDBEES",
    "SILVERBEES"
]

df = df[["Date"] + etfs]


# --------------------------------------------------
# 5. CHECK MISSING VALUES
# --------------------------------------------------

print("\n" + "=" * 70)
print("MISSING VALUES")
print("=" * 70)

print(df.isnull().sum())


# --------------------------------------------------
# 6. CHECK DUPLICATES
# --------------------------------------------------

print("\n" + "=" * 70)
print("DUPLICATE DATES")
print("=" * 70)

print(df["Date"].duplicated().sum())


# --------------------------------------------------
# 7. CHECK DATA TYPES
# --------------------------------------------------

print("\n" + "=" * 70)
print("DATA TYPES")
print("=" * 70)

print(df.dtypes)


# --------------------------------------------------
# 8. CHECK DATE RANGE
# --------------------------------------------------

print("\n" + "=" * 70)
print("DATE RANGE")
print("=" * 70)

print("Start:", df["Date"].min().date())
print("End  :", df["Date"].max().date())

print("Number of months:", len(df))


# --------------------------------------------------
# 9. CHECK NEGATIVE / ZERO PRICES
# --------------------------------------------------

print("\n" + "=" * 70)
print("ZERO / NEGATIVE VALUES")
print("=" * 70)

for etf in etfs:
    invalid = (df[etf] <= 0).sum()
    print(f"{etf}: {invalid}")


# --------------------------------------------------
# 10. SAVE CLEAN DATASET
# --------------------------------------------------

output_path = r"C:\Users\Sathya\ETF_dataset\ETF_monthly_clean.csv"

df.to_csv(output_path, index=False)

print("\n" + "=" * 70)
print("CLEANING COMPLETE")
print("=" * 70)

print("Saved to:")
print(output_path)