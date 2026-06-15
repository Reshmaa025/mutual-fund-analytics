# Bluestock Mutual Fund Analytics Capstone Project

## Project Overview

This project focuses on analyzing mutual fund performance using data analytics, risk analysis, and business intelligence techniques. The project implements an end-to-end ETL pipeline, performs exploratory and advanced analytics, and visualizes insights using Power BI dashboards.

## Objectives

* Build an ETL pipeline for mutual fund datasets.
* Perform Exploratory Data Analysis (EDA).
* Calculate performance metrics such as CAGR and Sharpe Ratio.
* Conduct risk analysis using Maximum Drawdown, VaR, and CVaR.
* Develop an interactive Power BI dashboard.
* Generate actionable investment insights.

## Technology Stack

* Python
* Pandas
* NumPy
* SQLite
* SQL
* Power BI
* Matplotlib
* Seaborn

## Dataset Description

The project uses the following datasets:

1. Fund Master Data
2. NAV History
3. AUM Data
4. SIP Inflows
5. Investor Transactions
6. Portfolio Holdings
7. Benchmark Indices

## Project Structure

project/
│
├── data/
├── notebooks/
├── dashboard/
├── screenshots/
├── reports/
├── run_pipeline.py
├── README.md
└── Final_Report.pdf

## ETL Process

### Extract

Data is collected from multiple CSV files.

### Transform

* Missing value handling
* Data cleaning
* Feature engineering
* Return calculations

### Load

Processed data is loaded into SQLite database and Power BI.

## How to Run

### Install Dependencies

pip install -r requirements.txt

### Execute ETL Pipeline

python run_pipeline.py

## Dashboard

Open the Power BI dashboard file:

Bluestock_MF.pbix

## Key Findings

* ICICI Bluechip and Nippon Large Cap delivered strong performance.
* SIP inflows increased steadily over time.
* Banking and IT sectors dominated portfolio allocation.
* Risk-adjusted metrics provided better fund evaluation.

## Future Enhancements

* Real-time market data integration
* Machine learning-based prediction models
* Automated dashboard refresh
* Cloud deployment
