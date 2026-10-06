import pandas as pd

# ============================================================
# 1. LOAD CLEAN MONTHLY DATA
# ============================================================

file_path = r"C:\Users\Sathya\ETF_dataset\ETF_monthly_clean.csv"

df = pd.read_csv(file_path)

df["Date"] = pd.to_datetime(df["Date"])

# ============================================================
# 2. ETF LIST
# ============================================================

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

# Fixed monthly SIP
SIP_AMOUNT = 5000

# ============================================================
# 3. CREATE SIP TRANSACTION DATA
# ============================================================

sip_records = []

for etf in etfs:

    cumulative_units = 0

    for _, row in df.iterrows():

        date = row["Date"]
        price = row[etf]

        # Units purchased this month
        units_purchased = SIP_AMOUNT / price

        # Update cumulative units
        cumulative_units += units_purchased

        # Record transaction
        sip_records.append({
            "Date": date,
            "ETF": etf,
            "SIP_Investment": SIP_AMOUNT,
            "Adjusted_Close": price,
            "Units_Purchased": units_purchased,
            "Cumulative_Units": cumulative_units
        })


# Convert to DataFrame
sip_df = pd.DataFrame(sip_records)

# ============================================================
# 4. CALCULATE FINAL VALUE
# ============================================================

summary = []

for etf in etfs:

    etf_data = sip_df[sip_df["ETF"] == etf].copy()

    total_invested = etf_data["SIP_Investment"].sum()

    cumulative_units = etf_data["Units_Purchased"].sum()

    final_price = etf_data.iloc[-1]["Adjusted_Close"]

    final_value = cumulative_units * final_price

    absolute_profit = final_value - total_invested

    absolute_return = (
        absolute_profit / total_invested
    ) * 100

    summary.append({
        "ETF": etf,
        "Total_Invested": total_invested,
        "Cumulative_Units": cumulative_units,
        "Final_Price": final_price,
        "Final_Portfolio_Value": final_value,
        "Absolute_Profit": absolute_profit,
        "Absolute_Return_%": absolute_return
    })


summary_df = pd.DataFrame(summary)

# ============================================================
# 5. DISPLAY RESULTS
# ============================================================

print("=" * 80)
print("SIP SIMULATION RESULTS")
print("=" * 80)

print("\nMonthly SIP:", f"₹{SIP_AMOUNT:,}")

print("Number of months:", len(df))

print(
    "Total investment per ETF:",
    f"₹{SIP_AMOUNT * len(df):,}"
)

print("\n")

print(
    summary_df.to_string(
        index=False,
        float_format=lambda x: f"{x:,.4f}"
    )
)

# ============================================================
# 6. SAVE TRANSACTION DATA
# ============================================================

transaction_path = (
    r"C:\Users\Sathya\ETF_dataset"
    r"\ETF_SIP_transactions.csv"
)

sip_df.to_csv(
    transaction_path,
    index=False
)

# ============================================================
# 7. SAVE SUMMARY
# ============================================================

summary_path = (
    r"C:\Users\Sathya\ETF_dataset"
    r"\ETF_SIP_summary.csv"
)

summary_df.to_csv(
    summary_path,
    index=False
)

# ============================================================
# 8. COMPLETION MESSAGE
# ============================================================

print("\n" + "=" * 80)
print("SIP SIMULATION COMPLETE")
print("=" * 80)

print("\nTransaction dataset:")
print(transaction_path)

print("\nSummary dataset:")
print(summary_path)