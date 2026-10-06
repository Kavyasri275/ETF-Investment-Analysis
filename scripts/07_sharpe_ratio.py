import pandas as pd
import numpy as np

# ============================================================
# 1. FILE PATHS
# ============================================================

returns_file = r"C:\Users\Sathya\ETF_dataset\ETF_monthly_returns.csv"

# Annual risk-free rate assumption
RISK_FREE_RATE = 0.06

# ============================================================
# 2. LOAD MONTHLY RETURNS
# ============================================================

returns = pd.read_csv(returns_file)

returns["Date"] = pd.to_datetime(returns["Date"])

return_data = returns.drop(columns=["Date"])

# ============================================================
# 3. CALCULATE ANNUALIZED RETURN
# ============================================================

# Average monthly return
average_monthly_return = return_data.mean()

# Annualized return
annualized_return = average_monthly_return * 12

# ============================================================
# 4. CALCULATE ANNUALIZED VOLATILITY
# ============================================================

monthly_volatility = return_data.std()

annualized_volatility = monthly_volatility * np.sqrt(12)

# ============================================================
# 5. CALCULATE SHARPE RATIO
# ============================================================

sharpe_ratio = (
    annualized_return - RISK_FREE_RATE
) / annualized_volatility

# ============================================================
# 6. CREATE RESULTS TABLE
# ============================================================

results = pd.DataFrame({
    "ETF": return_data.columns,
    "Annualized_Return_%": annualized_return.values * 100,
    "Annualized_Volatility_%": annualized_volatility.values * 100,
    "Risk_Free_Rate_%": RISK_FREE_RATE * 100,
    "Sharpe_Ratio": sharpe_ratio.values
})

# ============================================================
# 7. DISPLAY RESULTS
# ============================================================

print("\n")
print("=" * 80)
print("SHARPE RATIO ANALYSIS")
print("=" * 80)

print(
    results[
        [
            "ETF",
            "Annualized_Return_%",
            "Annualized_Volatility_%",
            "Risk_Free_Rate_%",
            "Sharpe_Ratio"
        ]
    ].to_string(index=False)
)

# ============================================================
# 8. SAVE RESULTS
# ============================================================

output_file = (
    r"C:\Users\Sathya\ETF_dataset\ETF_sharpe_results.csv"
)

results.to_csv(
    output_file,
    index=False
)

print("\nSharpe ratio results saved to:")
print(output_file)