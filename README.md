# Super-stores-Dataset
# Sales Analytics Dashboard

An end-to-end data analytics project on 9,792 retail orders.
Covers data cleaning, SQL analysis, and an interactive Streamlit dashboard.

**Live demo:**  http://localhost:8501/

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
