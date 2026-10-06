import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="ETF SIP Investment Analyzer",
    page_icon="📊",
    layout="wide"
)


# ============================================================
# FILE PATHS
# ============================================================

BASE_PATH = r"C:\Users\Sathya\ETF_dataset"

PRICE_FILE = rf"{BASE_PATH}\ETF_monthly_clean.csv"
XIRR_FILE = rf"{BASE_PATH}\ETF_XIRR_results.csv"
VOLATILITY_FILE = rf"{BASE_PATH}\ETF_volatility_results.csv"
DRAWDOWN_FILE = rf"{BASE_PATH}\ETF_max_drawdown_results.csv"
SHARPE_FILE = rf"{BASE_PATH}\ETF_sharpe_results.csv"
CORRELATION_FILE = rf"{BASE_PATH}\ETF_correlation_matrix.csv"


# ============================================================
# LOAD DATA
# ============================================================

prices = pd.read_csv(PRICE_FILE)
prices["Date"] = pd.to_datetime(prices["Date"])

xirr = pd.read_csv(XIRR_FILE)
volatility = pd.read_csv(VOLATILITY_FILE)
drawdown = pd.read_csv(DRAWDOWN_FILE)
sharpe = pd.read_csv(SHARPE_FILE)

correlation = pd.read_csv(
    CORRELATION_FILE,
    index_col=0
)


# ============================================================
# ETF LIST
# ============================================================

etfs = [
    col for col in prices.columns
    if col != "Date"
]


# ============================================================
# TITLE
# ============================================================

st.title("📊 ETF SIP Investment Analyzer")

st.write(
    "Compare historical SIP performance, risk and "
    "diversification across selected ETFs."
)


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.header("Investment Settings")

# USER-CONTROLLED SIP AMOUNT
sip_amount = st.sidebar.number_input(
    "Monthly SIP Amount (₹)",
    min_value=100,
    max_value=1000000,
    value=5000,
    step=500
)

selected_etf = st.sidebar.selectbox(
    "Select ETF",
    etfs
)

st.sidebar.markdown("---")

st.sidebar.write(
    f"Investment Period: "
    f"{prices['Date'].min().strftime('%b %Y')} - "
    f"{prices['Date'].max().strftime('%b %Y')}"
)

number_of_months = len(prices)

st.sidebar.write(
    f"Number of Months: {number_of_months}"
)


# ============================================================
# DYNAMIC SIP CALCULATION
# ============================================================

selected_prices = prices[
    ["Date", selected_etf]
].copy()

selected_prices["Units_Purchased"] = (
    sip_amount / selected_prices[selected_etf]
)

selected_prices["Cumulative_Units"] = (
    selected_prices["Units_Purchased"].cumsum()
)

selected_prices["Portfolio_Value"] = (
    selected_prices["Cumulative_Units"]
    * selected_prices[selected_etf]
)

total_invested = (
    sip_amount * number_of_months
)

final_value = (
    selected_prices["Portfolio_Value"].iloc[-1]
)

absolute_profit = (
    final_value - total_invested
)

absolute_return = (
    absolute_profit / total_invested
) * 100


# ============================================================
# XIRR
# ============================================================

# XIRR is scale-independent, so use the historical
# XIRR calculated earlier for the selected ETF.

selected_xirr = xirr.loc[
    xirr["ETF"] == selected_etf,
    "XIRR_Percentage"
].iloc[0]


# ============================================================
# RISK METRICS
# ============================================================

selected_volatility = volatility.loc[
    volatility["ETF"] == selected_etf,
    "Annualized_Volatility_%"
].iloc[0]


selected_drawdown = drawdown.loc[
    drawdown["ETF"] == selected_etf,
    "Maximum_Drawdown_%"
].iloc[0]


selected_sharpe = sharpe.loc[
    sharpe["ETF"] == selected_etf,
    "Sharpe_Ratio"
].iloc[0]


# ============================================================
# OVERVIEW METRICS
# ============================================================

st.subheader(f"{selected_etf} — SIP Performance")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Monthly SIP",
        f"₹{sip_amount:,.0f}"
    )

with col2:
    st.metric(
        "Total Invested",
        f"₹{total_invested:,.0f}"
    )

with col3:
    st.metric(
        "Final Portfolio Value",
        f"₹{final_value:,.0f}"
    )

with col4:
    st.metric(
        "Absolute Profit",
        f"₹{absolute_profit:,.0f}"
    )


# ============================================================
# RETURN METRICS
# ============================================================

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Absolute Return",
        f"{absolute_return:.2f}%"
    )

with col2:
    st.metric(
        "XIRR",
        f"{selected_xirr:.2f}%"
    )

with col3:
    st.metric(
        "Annualized Volatility",
        f"{selected_volatility:.2f}%"
    )

with col4:
    st.metric(
        "Sharpe Ratio",
        f"{selected_sharpe:.2f}"
    )


# ============================================================
# SIP GROWTH CHART
# ============================================================

st.subheader("📈 SIP Portfolio Growth")

fig, ax = plt.subplots(figsize=(12, 5))

ax.plot(
    selected_prices["Date"],
    selected_prices["Portfolio_Value"]
)

ax.set_xlabel("Date")
ax.set_ylabel("Portfolio Value (₹)")
ax.set_title(
    f"{selected_etf} SIP Growth"
)

ax.grid(
    True,
    alpha=0.3
)

plt.tight_layout()

st.pyplot(fig)


# ============================================================
# INVESTMENT DETAILS
# ============================================================

st.subheader("💰 Investment Summary")

summary_data = pd.DataFrame({
    "Metric": [
        "Monthly SIP",
        "Number of Months",
        "Total Invested",
        "Final Portfolio Value",
        "Absolute Profit",
        "Absolute Return",
        "XIRR"
    ],
    "Value": [
        f"₹{sip_amount:,.0f}",
        number_of_months,
        f"₹{total_invested:,.2f}",
        f"₹{final_value:,.2f}",
        f"₹{absolute_profit:,.2f}",
        f"{absolute_return:.2f}%",
        f"{selected_xirr:.2f}%"
    ]
})

st.dataframe(
    summary_data,
    use_container_width=True,
    hide_index=True
)


# ============================================================
# RISK ANALYSIS
# ============================================================

st.subheader("⚠️ Risk Analysis")

risk_data = pd.DataFrame({
    "Risk Measure": [
        "Annualized Volatility",
        "Maximum Drawdown",
        "Sharpe Ratio"
    ],
    "Value": [
        f"{selected_volatility:.2f}%",
        f"{selected_drawdown:.2f}%",
        f"{selected_sharpe:.2f}"
    ]
})

st.dataframe(
    risk_data,
    use_container_width=True,
    hide_index=True
)


# ============================================================
# CORRELATION HEATMAP
# ============================================================

st.subheader("🔗 ETF Correlation Matrix")

fig2, ax2 = plt.subplots(
    figsize=(12, 8)
)

image = ax2.imshow(
    correlation.values,
    aspect="auto"
)

ax2.set_xticks(
    range(len(correlation.columns))
)

ax2.set_yticks(
    range(len(correlation.index))
)

ax2.set_xticklabels(
    correlation.columns,
    rotation=45,
    ha="right"
)

ax2.set_yticklabels(
    correlation.index
)

for i in range(len(correlation.index)):

    for j in range(len(correlation.columns)):

        ax2.text(
            j,
            i,
            f"{correlation.iloc[i, j]:.2f}",
            ha="center",
            va="center"
        )

ax2.set_title(
    "ETF Monthly Return Correlation"
)

fig2.colorbar(
    image,
    ax=ax2,
    label="Correlation"
)

plt.tight_layout()

st.pyplot(fig2)


# ============================================================
# ETF COMPARISON
# ============================================================

st.subheader("📊 ETF Performance Comparison")

comparison = xirr[
    [
        "ETF",
        "XIRR_Percentage"
    ]
].copy()

comparison = comparison.merge(
    volatility[
        [
            "ETF",
            "Annualized_Volatility_%"
        ]
    ],
    on="ETF"
)

comparison = comparison.merge(
    drawdown[
        [
            "ETF",
            "Maximum_Drawdown_%"
        ]
    ],
    on="ETF"
)

comparison = comparison.merge(
    sharpe[
        [
            "ETF",
            "Sharpe_Ratio"
        ]
    ],
    on="ETF"
)

comparison.columns = [
    "ETF",
    "XIRR (%)",
    "Annualized Volatility (%)",
    "Maximum Drawdown (%)",
    "Sharpe Ratio"
]

st.dataframe(
    comparison,
    use_container_width=True,
    hide_index=True
)


# ============================================================
# FOOTER
# ============================================================

st.markdown("---")

st.caption(
    "Historical analysis based on monthly ETF data "
    "from March 2022 to September 2026."
)