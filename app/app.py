import streamlit as st
import pandas as pd
import plotly.express as px
import os

# Creating an absolute path to the cleaned CSV
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSV_PATH = os.path.join(BASE_DIR, 'data', 'processed', 'sales_clean.csv')

@st.cache_data
def load_data():
    df = pd.read_csv(CSV_PATH)
    df['order_date'] = pd.to_datetime(df['order_date'])
    return df

df = load_data()

# Sidebar filters 
st.sidebar.header("Filters")

years = sorted(df['order_year'].unique())
selected_years = st.sidebar.multiselect(
    "Select Year",
    options=years,
    default=years
)

regions = sorted(df['region'].unique())
selected_regions = st.sidebar.multiselect(
    "Select Region",
    options=regions,
    default=regions 
)

categories = sorted(df['category'].unique())
selected_categories = st.sidebar.multiselect(
    "Select Category",
    options=categories,
    default=categories
)

# Filter the dataframe based on selections
filtered_df = df[
    (df['order_year'].isin(selected_years)) &
    (df['region'].isin(selected_regions)) &
    (df['category'].isin(selected_categories))
]

#Page title 
st.title("Superstore Sales Analytics Dashboard")
st.markdown("Retail performance analysis across regions, categories and customers.")
st.divider()

# KPI row 
col1, col2, col3, col4 = st.columns(4)

col1.metric(
    label="Total Revenue",
    value=f"${filtered_df['sales'].sum():,.0f}"
)
col2.metric(
    label="Total Orders",
    value=f"{filtered_df['order_id'].nunique():,}"
)
col3.metric(
    label="Average Order Value",
    value=f"${filtered_df['sales'].mean():,.0f}"
)
col4.metric(
    label="Average Days to Ship",
    value=f"{filtered_df['days_to_ship'].mean():.1f} days"
)

st.divider()

# Monthly revenue trend 
monthly = filtered_df.groupby('order_month').agg(
    total_revenue=('sales', 'sum')
).reset_index()

fig1 = px.line(
    monthly,
    x='order_month',
    y='total_revenue',
    title='Monthly Revenue Trend',
    labels={'order_month': 'Month', 'total_revenue': 'Revenue ($)'}
)
fig1.update_layout(xaxis_tickangle=-45)
st.plotly_chart(fig1, use_container_width=True)

st.divider()

#Category and Region charts side by side 
col_a, col_b = st.columns(2)

with col_a:
    category_data = filtered_df.groupby('category').agg(
        total_revenue=('sales', 'sum')
    ).reset_index()

    fig2 = px.bar(
        category_data,
        x='category',
        y='total_revenue',
        title='Revenue by Category',
        color='category',
        labels={'total_revenue': 'Revenue ($)', 'category': 'Category'}
    )
    st.plotly_chart(fig2, use_container_width=True)

with col_b:
    region_data = filtered_df.groupby('region').agg(
        total_revenue=('sales', 'sum')
    ).reset_index()

    fig3 = px.pie(
        region_data,
        names='region',
        values='total_revenue',
        title='Revenue Share by Region'
    )
    st.plotly_chart(fig3, use_container_width=True)

st.divider()

# ── Ship mode analysis ─────────────────────────────────────
ship_data = filtered_df.groupby('ship_mode').agg(
    num_orders=('order_id', 'nunique'),
    avg_days=('days_to_ship', 'mean')
).reset_index()

fig4 = px.bar(
    ship_data,
    x='ship_mode',
    y='num_orders',
    title='Orders by Ship Mode',
    color='ship_mode',
    labels={'num_orders': 'Number of Orders', 'ship_mode': 'Ship Mode'}
)
st.plotly_chart(fig4, use_container_width=True)

st.divider()

# ── Top 10 customers ───────────────────────────────────────
top_customers = filtered_df.groupby(['customer_name', 'segment']).agg(
    lifetime_value=('sales', 'sum'),
    total_orders=('order_id', 'nunique')
).reset_index().sort_values('lifetime_value', ascending=False).head(10)

fig5 = px.bar(
    top_customers,
    x='lifetime_value',
    y='customer_name',
    orientation='h',
    color='segment',
    title='Top 10 Customers by Revenue',
    labels={'lifetime_value': 'Total Revenue ($)', 'customer_name': 'Customer'}
)
fig5.update_layout(yaxis={'categoryorder': 'total ascending'})
st.plotly_chart(fig5, use_container_width=True)
