import pandas as pd
import matplotlib.pyplot as plt

# ============================================================
# 1. FILE PATHS
# ============================================================

xirr_file = r"C:\Users\Sathya\ETF_dataset\ETF_XIRR_results.csv"
volatility_file = r"C:\Users\Sathya\ETF_dataset\ETF_volatility_results.csv"

# ============================================================
# 2. LOAD RESULTS
# ============================================================

xirr = pd.read_csv(xirr_file)
volatility = pd.read_csv(volatility_file)

# ============================================================
# 3. SELECT REQUIRED COLUMNS
# ============================================================

xirr_data = xirr[
    [
        "ETF",
        "XIRR_Percentage"
    ]
]

volatility_data = volatility[
    [
        "ETF",
        "Annualized_Volatility_%"
    ]
]

# ============================================================
# 4. MERGE RESULTS
# ============================================================

risk_return = xirr_data.merge(
    volatility_data,
    on="ETF",
    how="inner"
)

# ============================================================
# 5. DISPLAY DATA
# ============================================================

print("\n")
print("=" * 80)
print("RISK-RETURN ANALYSIS")
print("=" * 80)

print(
    risk_return.to_string(index=False)
)

# ============================================================
# 6. CREATE SCATTER PLOT
# ============================================================

plt.figure(figsize=(12, 8))

plt.scatter(
    risk_return["Annualized_Volatility_%"],
    risk_return["XIRR_Percentage"],
    s=100
)

# Add ETF labels
for _, row in risk_return.iterrows():

    plt.annotate(
        row["ETF"],
        (
            row["Annualized_Volatility_%"],
            row["XIRR_Percentage"]
        ),
        xytext=(6, 6),
        textcoords="offset points"
    )

# ============================================================
# 7. LABELS
# ============================================================

plt.xlabel("Annualized Volatility (%)")

plt.ylabel("XIRR / Annualized SIP Return (%)")

plt.title(
    "ETF Risk–Return Analysis"
)

plt.grid(
    True,
    alpha=0.3
)

plt.tight_layout()

# ============================================================
# 8. SAVE FIGURE
# ============================================================

output_file = (
    r"C:\Users\Sathya\ETF_dataset\ETF_risk_return_plot.png"
)

plt.savefig(
    output_file,
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("\nRisk-return plot saved to:")
print(output_file)

# ============================================================
# 9. SAVE COMBINED DATA
# ============================================================

csv_output = (
    r"C:\Users\Sathya\ETF_dataset\ETF_risk_return_data.csv"
)

risk_return.to_csv(
    csv_output,
    index=False
)

print("\nRisk-return data saved to:")
print(csv_output)