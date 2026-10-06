import pandas as pd

# ============================================================
# 1. FILE PATH
# ============================================================

price_file = r"C:\Users\Sathya\ETF_dataset\ETF_monthly_clean.csv"

# ============================================================
# 2. LOAD MONTHLY PRICES
# ============================================================

prices = pd.read_csv(price_file)

prices["Date"] = pd.to_datetime(prices["Date"])

prices = prices.sort_values("Date")

# ============================================================
# 3. CALCULATE MAXIMUM DRAWDOWN
# ============================================================

results = []

etfs = prices.columns.drop("Date")

for etf in etfs:

    # Monthly adjusted closing prices
    price = prices[etf]

    # Running historical peak
    running_peak = price.cummax()

    # Drawdown from previous peak
    drawdown = (price - running_peak) / running_peak

    # Maximum drawdown
    max_drawdown = drawdown.min()

    # Date of maximum drawdown
    max_drawdown_date = drawdown.idxmin()

    results.append({
        "ETF": etf,
        "Maximum_Drawdown": max_drawdown,
        "Maximum_Drawdown_%": max_drawdown * 100,
        "Drawdown_Date": prices.loc[
            max_drawdown_date, "Date"
        ]
    })

# ============================================================
# 4. CREATE RESULTS TABLE
# ============================================================

results = pd.DataFrame(results)

# ============================================================
# 5. DISPLAY RESULTS
# ============================================================

print("\n")
print("=" * 80)
print("MAXIMUM DRAWDOWN ANALYSIS")
print("=" * 80)

print(
    results[
        [
            "ETF",
            "Maximum_Drawdown_%",
            "Drawdown_Date"
        ]
    ].to_string(index=False)
)

# ============================================================
# 6. SAVE RESULTS
# ============================================================

output_file = (
    r"C:\Users\Sathya\ETF_dataset\ETF_max_drawdown_results.csv"
)

results.to_csv(
    output_file,
    index=False
)

print("\nMaximum drawdown results saved to:")
print(output_file)