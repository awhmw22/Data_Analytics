# Smart Retail Optimization System

An end‑to‑end data analytics project that leverages Excel, SQL, Python and Power BI to deliver actionable insights for a retail business. This system helps solve common retail challenges—overstocking, stockouts, suboptimal pricing and low customer engagement—by integrating cleaned transactional data, advanced analytics and interactive dashboards.

---

## 📖 Overview

Retailers today must balance inventory levels, pricing strategies and customer engagement across online and brick‑and‑mortar channels. The **Smart Retail Optimization System**:

1. **Ingests & Cleans** raw sales, customer, product, inventory, store and supplier data in PostgreSQL  
2. **Explores & Models** data in Python to generate forecasts, RFM/CLV segments, reorder points and inventory turnover ratios  
3. **Visualizes** key metrics—revenue, profit, customer behavior and supply‑chain health—in a multi‑page Power BI dashboard  

Whether you want to reduce waste, improve profit margins or target high‑value customers, this project provides a fully reproducible pipeline and a portfolio‑worthy deliverable.

---

## 🚀 Features

- **Data Ingestion & ETL**  
  - Python scripts (`src/data_ingestion.py`, `src/generate_data.py`) load and clean CSVs into PostgreSQL  
  - Schema with normalized tables: `Products`, `Customers`, `Sales`, `Inventory`, `Stores`, `Suppliers`  

- **Data Cleaning**  
  - Jupyter notebooks + Python modules to remove duplicates, fix data types, compute `Clean_*` tables  

- **Exploratory Data Analysis**  
  - Product profitability, sales trends, customer demographics and behavior using Pandas & Matplotlib  

- **Advanced Metrics**  
  - **Customer Lifetime Value (CLV)** segments  
  - **RFM scoring** (Recency, Frequency, Monetary)  
  - **Reorder points** (average recent demand)  
  - **Inventory turnover** ratios  

- **Interactive Dashboard** (Power BI)  
  - **Page 1: Overview** — KPIs, sales trends, top products, channel & category breakdown  
  - **Page 2: Customer Insights** — CLV tile slicer, order frequency distribution, top customers  
  - **Page 3: Product & Supplier Insights** — RFM segments, low stock alerts, supplier profitability  

---

## 🗂️ Directory Structure

smart_retail_optimization/
├── data/ # raw CSV files
├── notebooks/ # EDA & modeling notebooks
├── src/
│ ├── etl/ # cleaning scripts (clean_sales.py, clean_customers.py, …)
│ ├── eda/ # exploratory analysis scripts (eda_products.py, eda_customers.py, …)
│ ├── utils.py # DB connection helper
│ ├── data_ingestion.py # load CSV → PostgreSQL
│ └── generate_data.py # synthetic data generator
├── sql/
│ ├── schema.sql # DDL for PostgreSQL tables
│ └── queries.sql # useful analytical queries
├── powerbi/ # Power BI .pbix files
├── reports/ # exported PDF reports
├── requirements.txt # Python dependencies
└── README.md # Project overview & instructions


---

## ⚙️ Tech Stack

- **Database:** PostgreSQL  
- **Scripting & Analysis:** Python (Pandas, SQLAlchemy, scikit‑learn, Prophet)  
- **Visualization:** Power BI (DAX measures, interactive slicers)  
- **Version Control:** Git & GitHub  

---

## 🛠️ Setup & Usage

1. **Clone the repo**  
   ```bash
   git clone https://github.com/yourusername/smart_retail_optimization.git
   cd smart_retail_optimization

   Install dependencies
pip install -r requirements.txt
Configure PostgreSQL

Create database smart_retail_db

Populate .env with DB credentials

Initialize schema & seed data

psql -U <user> -d smart_retail_db -f sql/schema.sql
python src/generate_data.py
python src/data_ingestion.py

Run cleaning & EDA
python src/etl/clean_sales.py
python src/eda/eda_products.py

Open Power BI
Import powerbi/smart_retail_dashboard.pbix

Connect to your Postgres DB

Refresh visuals and explore!

📄 Reports
Detailed PDF is available in reports/ summarizing business problem, methodology, insights and recommendations.

🤝 Contributing
Feel free to open issues or submit pull requests! Suggestions for new analytics, modeling techniques or dashboard improvements are very welcome.
