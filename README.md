# ETF Investment Analysis

A Python-based financial analytics project for evaluating the performance, risk, and investment characteristics of multiple Indian Exchange Traded Funds (ETFs).

## Project Overview

This project analyzes historical ETF market data and performs multiple financial analyses to understand investment performance, risk, diversification, and portfolio behavior.

The project covers:

- Data cleaning and preprocessing
- Monthly return analysis
- SIP simulation
- XIRR calculation
- Volatility analysis
- Maximum drawdown analysis
- Sharpe ratio analysis
- Correlation analysis
- Portfolio analysis
- Risk-return analysis

## ETFs Analyzed

The project analyzes the following ETFs:

- NIFTYBEES
- BANKBEES
- JUNIORBEES
- ITBEES
- PHARMABEES
- AUTOBEES
- INFRABEES
- GOLDBEES
- SILVERBEES

## Project Workflow

```text
Raw ETF Data
     ↓
Data Cleaning
     ↓
Monthly Data Preparation
     ↓
Return & Risk Analysis
     ↓
SIP / XIRR Analysis
     ↓
Portfolio Analysis
     ↓
Risk-Return & Correlation Analysis
     ↓
Results & Visualizations
```

## Analysis Modules

### 1. Data Cleaning

Historical ETF data is cleaned and prepared for subsequent analysis.

### 2. Monthly Returns

Monthly adjusted closing prices are used to calculate monthly returns for each ETF.

### 3. SIP Simulation

The project simulates systematic monthly investments and calculates:

- Total investment
- Final portfolio value
- Absolute return
- Investment growth

The SIP amount can be configured rather than being permanently fixed.

### 4. XIRR

XIRR is calculated to estimate the annualized return of periodic investments while accounting for the timing of cash flows.

### 5. Volatility

Monthly and annualized volatility are calculated to measure the variability and risk of ETF returns.

### 6. Maximum Drawdown

Maximum drawdown measures the largest decline from a historical peak to a subsequent trough.

### 7. Sharpe Ratio

The Sharpe ratio is used to evaluate risk-adjusted investment performance.

### 8. Correlation Analysis

Correlation analysis measures how ETF returns move relative to one another and helps evaluate diversification opportunities.

### 9. Portfolio Analysis

Multiple ETFs are combined to analyze portfolio-level performance and monthly behavior.

### 10. Risk-Return Analysis

ETF risk and return characteristics are compared to understand the relationship between potential return and investment risk.

## Project Structure

```text
ETF-Investment-Analysis/
│
├── data/
│   ├── ETF daily datasets
│   ├── Combined ETF dataset
│   └── Monthly datasets
│
├── scripts/
│   ├── 01_data_cleaning.py
│   ├── 02_monthly_returns.py
│   ├── 03_sip_simulation.py
│   ├── 04_xirr_calculation.py
│   ├── 05_volatility.py
│   ├── 06_max_drawdown.py
│   ├── 07_sharpe_ratio.py
│   ├── 08_correlation_analysis.py
│   ├── 09_correlation_heatmap.py
│   ├── 10_portfolio_analysis.py
│   ├── 11_risk_return_analysis.py
│   └── app.py
│
├── results/
│   ├── Analysis CSV files
│   └── Visualization outputs
│
└── README.md
```

## Technologies Used

- Python
- Pandas
- NumPy
- NumPy Financial
- Matplotlib
- CSV
- Financial Data Analysis
- Quantitative Analysis

## Key Outputs

The project generates results covering:

- Monthly ETF returns
- SIP investment performance
- XIRR
- Volatility
- Maximum drawdown
- Sharpe ratio
- ETF correlation
- Portfolio performance
- Risk-return characteristics

## Results and Visualizations

The `results/` directory contains the generated analysis outputs, including:

- Correlation matrix
- Correlation heatmap
- Maximum drawdown results
- Monthly returns
- Portfolio analysis
- Risk-return analysis
- Sharpe ratio results
- SIP results
- Volatility results
- XIRR results

## Future Improvements

- Interactive investment calculator
- User-configurable SIP amount
- Portfolio optimization
- Risk-adjusted portfolio recommendations
- Additional financial metrics
- Interactive dashboard
- Web-based deployment
- Automated ETF data updates

## Disclaimer

This project is intended for educational and analytical purposes only. The analysis does not constitute financial or investment advice.
