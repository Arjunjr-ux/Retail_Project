# 📊 Retail Sales Analytics & Interactive Dashboard

An end-to-end Data Analytics project that involves data cleaning, exploratory analysis, KPI calculation, and building an interactive dashboard using Streamlit.

---

## 🚀 Project Overview

The goal of this project is to transform raw retail sales data into meaningful business insights through:

- Data Cleaning and Preprocessing
- Sales Trend Analysis
- KPI Calculation
- Interactive Dashboard Development

---

## 🛠️ Tools & Technologies Used

- Python
- Pandas
- Plotly
- Streamlit
- Jupyter Notebook
- VS Code
- Git & GitHub

---

## 📂 Dataset Overview

The dataset contains approximately **80,000 rows** and **33 columns**, including:

- Customer Information
- Product Information
- Sales Data
- Profit Data
- Region Details
- Category and Subcategory Information
- Return Status
- Payment Methods

---

## 🧹 Data Cleaning

The following cleaning steps were performed:

- Removed duplicate rows
- Standardized date formats
- Fixed inconsistent text values
- Handled missing values
- Standardized return flags
- Validated quantity values
- Created a cleaned dataset (`retail_sales_clean.csv`)

---

## 📈 Trend Analysis

The following analyses were performed:

### Monthly Sales Trend
Identified seasonal patterns in sales.

### Sales and Profit by Region
Compared regional performance.

### Sales by Category and Subcategory
Identified best-performing products.

### Year-over-Year Growth
Analyzed business growth over time.

---

## 📊 Key Performance Indicators (KPIs)

- Total Revenue
- Total Profit
- Profit Margin
- Average Order Value (AOV)
- Top 10 Customers
- Return Rate
- Repeat Customer Rate

---

## 📉 Interactive Dashboard

The dashboard was developed using **Streamlit** and includes:

### KPI Cards
- Revenue
- Profit
- Orders
- Average Order Value

### Filters
- Region
- Category
- Segment

### Interactive Charts
- Monthly Sales Trend
- Sales & Profit by Region
- Sales Distribution by Category
- Top 10 Customers

### Data Table
- Interactive dataset exploration

---

## 📁 Project Structure

```text
Retail_Project/
│
├── analysis.ipynb
├── dashboard.py
├── retail_sales.csv
├── retail_sales_clean.csv
├── README.md
```

---

## ▶️ Running the Project

Clone the repository:

```bash
git clone https://github.com/Arjunjr-ux/Retail_Project.git
```

Navigate to the project folder:

```bash
cd Retail_Project
```

Install dependencies:

```bash
pip install pandas plotly streamlit
```

Run the Streamlit dashboard:

```bash
streamlit run dashboard.py
```

---

## 📌 Key Insights

- Sales exhibited seasonal patterns.
- Certain regions generated higher revenue and profit.
- Some categories outperformed others.
- Top customers contributed significantly to revenue.
- Year-over-year analysis revealed business growth trends.

---

## 🎯 Conclusion

This project demonstrates the complete data analytics workflow, from raw data cleaning to interactive dashboard development, providing valuable insights for business decision-making.

---

## 📷 Dashboard Preview

### Main Dashboard

![Dashboard](Retail_Project/Screenshots/Screenshot%202026-06-24%20041424.png)

### KPI Cards

![KPIs](Retail_Project/Screenshots/Screenshot%202026-06-24%20041455.png)

### Charts

![Charts](Retail_Project/Screenshots/Screenshot%202026-06-24%20041538.png)

## Live Dashboard

https://your-dashboard.streamlit.app

## 👨‍💻 Author

**Arjun Baburaj**

B.Sc Computer Science  
MES Kalladi College  
Kerala, India

---

⭐ If you found this project useful, consider giving it a star!
