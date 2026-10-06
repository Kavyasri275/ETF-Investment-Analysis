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

return_data = returns.drop(columns=["Date"])

# ============================================================
# 3. CREATE EQUAL WEIGHTS
# ============================================================

number_of_etfs = len(return_data.columns)

weight = 1 / number_of_etfs

weights = {
    etf: weight
    for etf in return_data.columns
}

print("\nETF Weights:")
print("=" * 50)

for etf, w in weights.items():
    print(f"{etf:<15} {w * 100:.2f}%")

# ============================================================
# 4. CALCULATE PORTFOLIO MONTHLY RETURN
# ============================================================

portfolio_returns = (
    return_data * weight
).sum(axis=1)

# ============================================================
# 5. ANNUALIZED PORTFOLIO RETURN
# ============================================================

annualized_return = (
    portfolio_returns.mean() * 12
)

# ============================================================
# 6. ANNUALIZED PORTFOLIO VOLATILITY
# ============================================================

annualized_volatility = (
    portfolio_returns.std() * np.sqrt(12)
)

# ============================================================
# 7. PORTFOLIO CUMULATIVE GROWTH
# ============================================================

cumulative_growth = (
    (1 + portfolio_returns).cumprod()
)

# ============================================================
# 8. PORTFOLIO MAXIMUM DRAWDOWN
# ============================================================

running_peak = cumulative_growth.cummax()

drawdown = (
    cumulative_growth - running_peak
) / running_peak

maximum_drawdown = drawdown.min()

# ============================================================
# 9. SHARPE RATIO
# ============================================================

risk_free_rate = 0.06

sharpe_ratio = (
    annualized_return - risk_free_rate
) / annualized_volatility

# ============================================================
# 10. CREATE MONTHLY PORTFOLIO DATAFRAME
# ============================================================

portfolio_data = pd.DataFrame({
    "Date": returns["Date"],
    "Portfolio_Return": portfolio_returns,
    "Cumulative_Growth": cumulative_growth,
    "Drawdown": drawdown
})

# ============================================================
# 11. DISPLAY PORTFOLIO RESULTS
# ============================================================

print("\n")
print("=" * 70)
print("EQUAL-WEIGHT PORTFOLIO ANALYSIS")
print("=" * 70)

print(f"Number of ETFs              : {number_of_etfs}")
print(f"Weight per ETF              : {weight * 100:.2f}%")
print(f"Annualized Return            : {annualized_return * 100:.2f}%")
print(f"Annualized Volatility        : {annualized_volatility * 100:.2f}%")
print(f"Maximum Drawdown             : {maximum_drawdown * 100:.2f}%")
print(f"Risk-Free Rate               : {risk_free_rate * 100:.2f}%")
print(f"Sharpe Ratio                 : {sharpe_ratio:.4f}")

# ============================================================
# 12. SAVE PORTFOLIO MONTHLY DATA
# ============================================================

monthly_output = (
    r"C:\Users\Sathya\ETF_dataset\ETF_portfolio_monthly.csv"
)

portfolio_data.to_csv(
    monthly_output,
    index=False
)

# ============================================================
# 13. SAVE PORTFOLIO SUMMARY
# ============================================================

summary = pd.DataFrame({
    "Metric": [
        "Number of ETFs",
        "Weight per ETF (%)",
        "Annualized Return (%)",
        "Annualized Volatility (%)",
        "Maximum Drawdown (%)",
        "Risk-Free Rate (%)",
        "Sharpe Ratio"
    ],
    "Value": [
        number_of_etfs,
        weight * 100,
        annualized_return * 100,
        annualized_volatility * 100,
        maximum_drawdown * 100,
        risk_free_rate * 100,
        sharpe_ratio
    ]
})

summary_output = (
    r"C:\Users\Sathya\ETF_dataset\ETF_portfolio_summary.csv"
)

summary.to_csv(
    summary_output,
    index=False
)

print("\nPortfolio monthly data saved to:")
print(monthly_output)

print("\nPortfolio summary saved to:")
print(summary_output)