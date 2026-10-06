import pandas as pd
import numpy as np
from scipy.optimize import brentq

# ============================================================
# 1. FILE PATHS
# ============================================================

transactions_file = r"C:\Users\Sathya\ETF_dataset\ETF_SIP_transactions.csv"
summary_file = r"C:\Users\Sathya\ETF_dataset\ETF_SIP_summary.csv"

# ============================================================
# 2. LOAD DATA
# ============================================================

transactions = pd.read_csv(transactions_file)
summary = pd.read_csv(summary_file)

transactions["Date"] = pd.to_datetime(transactions["Date"])

print("\nSummary columns:")
print(summary.columns.tolist())

# ============================================================
# 3. USE THE CORRECT FINAL VALUE COLUMN
# ============================================================

value_column = "Final_Portfolio_Value"

print("\nUsing final value column:", value_column)

# ============================================================
# 4. XNPV FUNCTION
# ============================================================

def xnpv(rate, cashflows, dates):

    start_date = dates.iloc[0]

    total = 0.0

    for cashflow, date in zip(cashflows, dates):

        days = (date - start_date).days

        total += cashflow / (
            (1 + rate) ** (days / 365.0)
        )

    return total


# ============================================================
# 5. XIRR FUNCTION
# ============================================================

def xirr(cashflows, dates):

    def objective(rate):
        return xnpv(rate, cashflows, dates)

    # Search between -99.99% and 1000%
    rate_grid = np.linspace(
        -0.9999,
        10,
        10000
    )

    previous_rate = rate_grid[0]
    previous_value = objective(previous_rate)

    for current_rate in rate_grid[1:]:

        current_value = objective(current_rate)

        # Check whether NPV changes sign
        if previous_value * current_value < 0:

            return brentq(
                objective,
                previous_rate,
                current_rate
            )

        previous_rate = current_rate
        previous_value = current_value

    return np.nan


# ============================================================
# 6. CALCULATE XIRR FOR EACH ETF
# ============================================================

results = []

etfs = transactions["ETF"].unique()

for etf in etfs:

    # Select one ETF
    etf_data = transactions[
        transactions["ETF"] == etf
    ].sort_values("Date").copy()

    # --------------------------------------------------------
    # SIP cash flows
    # --------------------------------------------------------

    # ₹5,000 invested every month
    dates = list(etf_data["Date"])

    cashflows = [-5000] * len(etf_data)

    # --------------------------------------------------------
    # Final portfolio value
    # --------------------------------------------------------

    final_value = summary.loc[
        summary["ETF"] == etf,
        value_column
    ].iloc[0]

    # Add final portfolio value on final date
    dates.append(
        etf_data["Date"].iloc[-1]
    )

    cashflows.append(
        final_value
    )

    # Convert to Series
    dates = pd.Series(dates)
    cashflows = pd.Series(cashflows)

    # --------------------------------------------------------
    # Calculate XIRR
    # --------------------------------------------------------

    annualized_return = xirr(
        cashflows,
        dates
    )

    results.append({
        "ETF": etf,
        "XIRR": annualized_return,
        "XIRR_Percentage": (
            annualized_return * 100
            if not pd.isna(annualized_return)
            else np.nan
        )
    })


# ============================================================
# 7. CREATE XIRR DATAFRAME
# ============================================================

xirr_results = pd.DataFrame(results)


# ============================================================
# 8. MERGE WITH SIP SUMMARY
# ============================================================

final_results = summary.merge(
    xirr_results,
    on="ETF",
    how="left"
)


# ============================================================
# 9. DISPLAY RESULTS
# ============================================================

print("\n")
print("=" * 80)
print("XIRR / ANNUALIZED SIP RETURN")
print("=" * 80)

display_columns = [
    "ETF",
    "Total_Invested",
    "Final_Portfolio_Value",
    "Absolute_Return_%",
    "XIRR_Percentage"
]

print(
    final_results[
        display_columns
    ].to_string(index=False)
)


# ============================================================
# 10. SAVE RESULTS
# ============================================================

output_file = (
    r"C:\Users\Sathya\ETF_dataset\ETF_XIRR_results.csv"
)

final_results.to_csv(
    output_file,
    index=False
)

print("\nXIRR results saved to:")
print(output_file)