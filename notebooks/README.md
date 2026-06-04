Mutual Fund Analytics Pipeline
📌 Project Overview

This project is an end-to-end data engineering and analytics pipeline built using Python, Pandas, SQLite, and SQL. It processes mutual fund datasets, cleans the data, builds a star schema, and performs financial analysis using SQL queries.

🎯 Objectives
Clean and preprocess mutual fund datasets
Build a structured star schema (Fact & Dimension tables)
Store processed data in SQLite database
Perform SQL-based financial analysis
Generate actionable insights from mutual fund data
🧱 Project Structure
mutual_fund_analytics/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   ├── 01_data_ingestion.ipynb
│   ├── 02_data_cleaning.ipynb
│   ├── 03_sql_database.ipynb
│   └── eda.ipynb
│
├── sql/
│   ├── schema.sql
│   ├── queries.sql
│
├── bluestock_mf.db
├── data_dictionary.md
└── README.md
🗄️ Database Schema
Fact Tables:
fact_nav → Daily NAV values of mutual funds
fact_transactions → Investor transactions (SIP, Lumpsum, Redemption)
fact_performance → Fund performance metrics
fact_aum → Assets Under Management
Dimension Tables:
dim_fund → Fund master details
dim_date → Date dimension for time-based analysis
🧹 Data Cleaning Steps
Parsed and standardized date formats
Removed duplicate records
Handled missing values
Ensured NAV values > 0
Standardized transaction types (SIP / Lumpsum / Redemption)
Validated expense ratio range (0.1% – 2.5%)
📊 SQL Analytics Performed
Top performing mutual funds
NAV trend analysis
SIP vs Redemption behavior
Transaction volume by state
Expense ratio vs performance
Risk-adjusted fund scoring
Investor activity insights
🛠️ Technologies Used
Python (Pandas, NumPy)
SQLite
SQLAlchemy
SQL
Jupyter Notebook
Git & GitHub
🚀 How to Run the Project
1. Clone repository
git clone https://github.com/your-username/mutual_fund_analytics.git
cd mutual_fund_analytics
2. Install dependencies
pip install -r requirements.txt
3. Run notebooks in order
01_data_ingestion → 02_data_cleaning → 03_sql_database
4. Execute SQL queries

Run queries from:

sql/queries.sql
📁 Output Files
Cleaned datasets → data/processed/
SQLite database → bluestock_mf.db
SQL schema → schema.sql
SQL queries → queries.sql
Data dictionary → data_dictionary.md
📌 Future Improvements
Add Power BI dashboard
Integrate live NAV API
Automate ETL pipeline
Add predictive analytics
👨‍💻 Author

Reshma J
Data Analytics Project
Focus: Data Engineering + SQL Analytics

⭐ Project Status

✔ Data Cleaning Completed
✔ Database Created
✔ SQL Analytics Done
✔ Project Ready for Submission