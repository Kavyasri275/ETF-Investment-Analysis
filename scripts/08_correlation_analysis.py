import pandas as pd

# ============================================================
# 1. FILE PATH
# ============================================================

returns_file = r"C:\Users\Sathya\ETF_dataset\ETF_monthly_returns.csv"

# ============================================================
# 2. LOAD MONTHLY RETURNS
# ============================================================

returns = pd.read_csv(returns_file)

returns["Date"] = pd.to_datetime(returns["Date"])

return_data = returns.drop(columns=["Date"])

# ============================================================
# 3. CALCULATE CORRELATION MATRIX
# ============================================================

correlation_matrix = return_data.corr()

# ============================================================
# 4. DISPLAY RESULTS
# ============================================================

print("\n")
print("=" * 100)
print("ETF CORRELATION MATRIX")
print("=" * 100)

print(
    correlation_matrix.round(4).to_string()
)

# ============================================================
# 5. SAVE CORRELATION MATRIX
# ============================================================

output_file = (
    r"C:\Users\Sathya\ETF_dataset\ETF_correlation_matrix.csv"
)

correlation_matrix.to_csv(output_file)

print("\nCorrelation matrix saved to:")
print(output_file)