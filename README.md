> Retail Sales Analysis Dashboard

>> Problem Statement
A retail store wants to improve its profitability and understand its performance over the last two years (2024-2025). The business faces several challenges:
1. Dirty Data: The sales records contain missing values, duplicates, formatting errors, and casing inconsistencies.
2. Sales Tracking: There is no clear overview of sales growth and seasonal demand patterns.
3. Product Performance: The team needs to identify top-performing categories/products and pinpoint areas of financial loss (leakage).
4. Regional & Customer Segmentation: The company wants to know which regions and customer segments are most lucrative for focused marketing.
5. Sales Forecasting: The sales team wants a data-driven monthly sales forecast for the next 6 months to manage inventory effectively.

---

>> Tools & Libraries Used
- Python 3.13: The primary language for analysis.
- Pandas: Data manipulation, cleaning, and aggregation.
- Numpy: Vectorized operations and missing value management.
- Matplotlib & Seaborn: Production-grade data visualizations (line charts, bar plots, heatmaps).
- Scikit-learn: Time-index feature engineering and Linear Regression modeling for trend forecasting.
- Jupyter Notebook: Interactive research and presentation environment.

---

>> Folder Structure
The repository is organized following clean, industry-standard project structures:
```text
retail-sales-analysis-dashboard/
│
├── data/
│   ├── raw/
│   │   └── retail_sales_data.csv       > Raw, noisy dataset (needs cleaning)
│   └── processed/
│       └── cleaned_sales_data.csv     > Cleaned dataset exported from the notebook
│
├── notebooks/
│   └── retail_sales_analysis.ipynb     > Jupyter Notebook containing data cleaning, EDA, & ML
│
├── images/
│   ├── monthly_sales_trend.png        > Monthly sales and profit line chart
│   ├── category_sales.png             > Product category performance with profit margins
│   ├── profit_by_region.png           > Regional profit contribution
│   ├── top_products.png               > Horizontal bar chart of top 10 products
│   ├── correlation_matrix.png         > Variable correlation heatmap
│   └── sales_forecast.png             > Linear regression forecast vs actual sales
│
├── .gitignore                          > Excludes virtual environments and cache
├── README.md                           > Professional project documentation
└── requirements.txt                    > Project dependencies
```

---

>> Key Insights & Business Findings
 Steady Growth Trend: Sales are showing an upward growth trend with an average monthly sales increase of approximately $1,500+ across the 24-month period.
 Q4 Holiday Season Surge: Strong seasonal spikes are observed during November and December, indicating that holiday campaigns and stock preparation should begin early in Q3.
 Technology is the Profit Engine: The Technology category generates the highest sales volume and holds the highest profit margins (~25%). The Dell XPS 13 Laptop is our most profitable product.
 Furniture Margin Concern: While Furniture has solid sales volume (ranked >2), it yields very low or negative profit margins on specific items (e.g. bookshelves and side tables), suggesting heavy discount rates or high shipping costs need adjustment.
 East & West Dominance: The East and West regions are the most profitable, whereas the South region significantly lags in sales and profitability.
 Consumer Segment Strength: The standard Consumer segment is the largest driver of both revenue and volume.

---

>> How to Run the Project

>>> Prerequisites
Make sure you have Python (version 3.10 or higher) installed.

>>> Step 1: Clone or Navigate to the Directory
```bash
cd retail-sales-analysis-dashboard
```

>>> Step 2: Create a Virtual Environment
```bash
> On Windows
python -m venv venv
venv\Scripts\activate

> On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

>>> Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

>>> Step 4: Open Jupyter Notebook
```bash
jupyter notebook
```
Navigate to the `notebooks/` folder and open `retail_sales_analysis.ipynb`. You can run all cells sequentially to reproduce the outputs and visualizations.

---
