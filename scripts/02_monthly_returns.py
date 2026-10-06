import pandas as pd

# --------------------------------------------------
# 1. LOAD CLEAN DATA
# --------------------------------------------------

file_path = r"C:\Users\Sathya\ETF_dataset\ETF_monthly_clean.csv"

df = pd.read_csv(file_path)

df["Date"] = pd.to_datetime(df["Date"])

# --------------------------------------------------
# 2. ETF LIST
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

# --------------------------------------------------
# 3. CALCULATE MONTHLY RETURNS
# --------------------------------------------------

returns = df.copy()

for etf in etfs:
    returns[etf] = df[etf].pct_change()

# --------------------------------------------------
# 4. REMOVE FIRST ROW
# --------------------------------------------------

# First month has no previous month,
# so its return cannot be calculated.

returns = returns.dropna().reset_index(drop=True)

# --------------------------------------------------
# 5. DISPLAY RESULTS
# --------------------------------------------------

print("=" * 70)
print("MONTHLY RETURNS")
print("=" * 70)

print("\nShape:")
print(returns.shape)

print("\nFirst 5 rows:")
print(returns.head())

print("\nLast 5 rows:")
print(returns.tail())

# --------------------------------------------------
# 6. CHECK MISSING VALUES
# --------------------------------------------------

print("\n" + "=" * 70)
print("MISSING VALUES")
print("=" * 70)

print(returns.isnull().sum())

# --------------------------------------------------
# 7. SAVE
# --------------------------------------------------

output_path = r"C:\Users\Sathya\ETF_dataset\ETF_monthly_returns.csv"

returns.to_csv(output_path, index=False)

print("\n" + "=" * 70)
print("RETURNS CALCULATION COMPLETE")
print("=" * 70)

print("Saved to:")
print(output_path)