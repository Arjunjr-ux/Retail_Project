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


df["OrderDate"] = pd.to_datetime(df["OrderDate"])

st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Sales Trend Over Time")
    sales_trend = (
        df.groupby(df["OrderDate"].dt.to_period("M"))["Sales"]
        .sum()
        .reset_index()
    )
    sales_trend["OrderDate"] = sales_trend["OrderDate"].dt.to_timestamp()

    fig_sales = px.line(
        sales_trend,
        x="OrderDate",
        y="Sales",
        labels={"OrderDate": "Month", "Sales": "Sales"},
        title="Monthly Sales Trend"
    )

    st.plotly_chart(fig_sales)


# Sales & Profit by Region

with col2:
    st.subheader("Sales and Profit by Region")

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

col3, col4 = st.columns(2)
with col3:
    st.subheader("Sales by Segment")
    segment_analysis = (
        df.groupby("Segment")["Sales"]
        .sum()
        .reset_index()
    )

    fig_segment = px.bar(
        segment_analysis,
        x="Segment",
        y="Sales",
        title="Sales by Segment"
    )

    st.plotly_chart(fig_segment)

with col4:
    st.subheader("Sales by Category")
    category_analysis = (
        df.groupby("Category")["Sales"]
        .sum()
        .reset_index()
    )

    fig_category = px.bar(
        category_analysis,
        x="Category",
        y="Sales",
        title="Sales by Category"
    )

    st.plotly_chart(fig_category)

st.subheader("Retail Data")

st.dataframe(df)