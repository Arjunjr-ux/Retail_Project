import streamlit as st
import pandas as pd
import plotly.express as px

# Load dataset
df = pd.read_csv("retail_sales_clean.csv")

# Dashboard title
st.title("Retail Sales Dashboard")

# KPI Calculations
revenue = df["Sales"].sum()
profit = df["Profit"].sum()
orders = df["OrderID"].nunique()
aov = revenue / orders

# KPI Cards
col1, col2, col3, col4 = st.columns(4)

col1.metric("Revenue", f"${revenue:,.2f}")
col2.metric("Profit", f"${profit:,.2f}")
col3.metric("Orders", orders)
col4.metric("AOV", f"${aov:,.2f}")

# Sidebar Filters
st.sidebar.header("Filters")

region = st.sidebar.selectbox(
    "Select Region",
    ["All"] + list(df["Region"].unique())
)

category = st.sidebar.selectbox(
    "Select Category",
    ["All"] + list(df["Category"].unique())
)

segment = st.sidebar.selectbox(
    "Select Segment",
    ["All"] + list(df["Segment"].unique())
)
# Apply Filters
if region != "All":
    df = df[df["Region"] == region]

if category != "All":
    df = df[df["Category"] == category]

if segment != "All":
    df = df[df["Segment"] == segment]

# Monthly Sales Trend
df["OrderDate"] = pd.to_datetime(df["OrderDate"])

monthly_sales = (
    df.groupby(df["OrderDate"].dt.to_period("M"))["Sales"]
    .sum()
)

monthly_sales.index = monthly_sales.index.to_timestamp()

fig = px.line(
    x=monthly_sales.index,
    y=monthly_sales.values,
    labels={"x": "Month", "y": "Sales"},
    title="Monthly Sales Trend"
)

st.plotly_chart(fig)

# Sales & Profit by Region
region_analysis = (
    df.groupby("Region")[["Sales", "Profit"]]
    .sum()
    .reset_index()
)

fig_region = px.bar(
    region_analysis,
    x="Region",
    y=["Sales", "Profit"],
    barmode="group",
    title="Sales and Profit by Region"
)

st.plotly_chart(fig_region)

category_analysis = (
    df.groupby("Category")["Sales"]
    .sum()
    .reset_index()
)

fig_category = px.pie(
    category_analysis,
    names="Category",
    values="Sales",
    title="Sales Distribution by Category"
)

st.plotly_chart(fig_category)

top_customers = (
    df.groupby("CustomerName")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

fig_customer = px.bar(
    top_customers,
    x="CustomerName",
    y="Sales",
    title="Top 10 Customers"
)

st.plotly_chart(fig_customer)

st.subheader("Retail Data")

st.dataframe(df)