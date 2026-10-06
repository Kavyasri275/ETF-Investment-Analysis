import pandas as pd
import numpy as np

# ============================================================
# 1. FILE PATH
# ============================================================

returns_file = r"C:\Users\Sathya\ETF_dataset\ETF_monthly_returns.csv"

# ============================================================
# 2. LOAD MONTHLY RETURNS
# ============================================================

returns = pd.read_csv(returns_file)

returns["Date"] = pd.to_datetime(returns["Date"])

# Remove Date column for calculations
return_data = returns.drop(columns=["Date"])

# ============================================================
# 3. CALCULATE MONTHLY VOLATILITY
# ============================================================

volatility = return_data.std()

# ============================================================
# 4. CALCULATE ANNUALIZED VOLATILITY
# ============================================================

# Monthly volatility × sqrt(12)
annualized_volatility = volatility * np.sqrt(12)

# ============================================================
# 5. CREATE RESULTS TABLE
# ============================================================

results = pd.DataFrame({
    "ETF": volatility.index,
    "Monthly_Volatility": volatility.values,
    "Annualized_Volatility": annualized_volatility.values
})

# Convert to percentage
results["Monthly_Volatility_%"] = (
    results["Monthly_Volatility"] * 100
)

results["Annualized_Volatility_%"] = (
    results["Annualized_Volatility"] * 100
)

# ============================================================
# 6. DISPLAY RESULTS
# ============================================================

print("\n")
print("=" * 80)
print("ETF VOLATILITY ANALYSIS")
print("=" * 80)

print(
    results[
        [
            "ETF",
            "Monthly_Volatility_%",
            "Annualized_Volatility_%"
        ]
    ].to_string(index=False)
)

# ============================================================
# 7. SAVE RESULTS
# ============================================================

output_file = (
    r"C:\Users\Sathya\ETF_dataset\ETF_volatility_results.csv"
)

results.to_csv(
    output_file,
    index=False
)

print("\nVolatility results saved to:")
print(output_file)