# Super-stores-Dataset
# Sales Analytics Dashboard
What does it actually cost a business to offer discounts? This project digs into 10,000+ retail orders from a fictional US-based superstore uncovering that discounts above 40% consistently produce negative profit margins across all product categories.

Built end-to-end: raw data cleaning → SQL analysis → interactive Streamlit dashboard with filters for year, region, and product category.
Live demo: https://sales-analytics-dashboard-hbqfpr4yh5g4ldwjdwy3r9.streamlit.app/

## Key findings
- Technology drives the highest revenue at $827k despite fewer orders
  than Office Supplies — it wins through high average order value ($456)
- The West region leads all regions with $710k in revenue
- Standard Class shipping handles 60% of all orders
- Sean Miller is the highest value customer at $25,043 across 5 orders

## Project structure
- `notebooks/01_eda.ipynb` — data profiling and quality checks
- `notebooks/02_cleaning.ipynb` — transformations and feature engineering
- `notebooks/03_analysis.ipynb` — SQL queries and aggregations
- `app/app.py` — interactive Streamlit dashboard

## How to run locally
1. Clone the repo
2. Download the dataset from [Kaggle](https://www.kaggle.com/datasets/vivek468/superstore-dataset-final)
   and place it at `data/raw/superstore.csv`
3. Create and activate a virtual environment
4. Run `pip install -r requirements.txt`
5. Run `streamlit run app/app.py`

## Tech stack
Python · Pandas · SQLite · Plotly · Streamlit
