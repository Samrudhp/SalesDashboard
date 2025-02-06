# Sales Data Analysis Project

## Overview
This project analyzes sales data to extract meaningful insights about business performance across different dimensions including time periods, product lines, territories, and customer segments.

## Dataset Features
The dataset contains 25 columns including:
- Order details (Order Number, Quantity, Price, Sales)
- Temporal information (Order Date, Quarter, Month, Year)
- Product information (Product Line, MSRP, Product Code)
- Customer information (Name, Contact Details)
- Geographic information (Address, City, State, Country, Territory)
- Deal categorization (Deal Size)

## Analysis and Visualizations

### Time-Based Analysis
1. Monthly Sales Trend
   - Line plot showing sales performance over time
   - Helps identify seasonal patterns and overall trends

2. Quarterly Performance
   - Bar plot of sales by quarter
   - Visualizes quarterly business cycles

3. Monthly Distribution
   - Bar and line plots of sales by month
   - Identifies peak sales months

4. Yearly Comparison
   - Bar plot showing year-over-year sales performance

### Product Analysis
1. Product Line Performance
   - Bar plot of sales by product line
   - Identifies best and worst performing product categories

### Geographic Analysis
1. Country-wise Sales
   - Bar plot showing sales distribution across countries
   - Highlights key markets

2. Territory Analysis
   - Bar plot of sales across different territories
   - Provides insights into regional performance

### Customer Analysis
1. Top 15 Customers
   - Horizontal bar plot of highest revenue-generating customers
   - Identifies key accounts

### Business Metrics
1. Deal Size Analysis
   - Bar plot showing sales distribution by deal size
   - Helps understand typical transaction values

2. Order Status Analysis
   - Bar plot of sales by order status
   - Monitors order fulfillment performance

### Statistical Analysis
1. Sales Distribution
   - Histogram with KDE showing sales distribution
   - Helps understand sales patterns and outliers

2. Correlation Matrix
   - Heatmap showing relationships between numerical variables
   - Identifies key business relationships

## Data Cleaning Steps
- Handled missing values in STATE and TERRITORY columns
- Filled missing ADDRESSLINE2 values
- Standardized date formats
- Removed null values where appropriate

## Libraries Used
- pandas: Data manipulation and analysis
- numpy: Numerical operations
- matplotlib: Basic plotting
- seaborn: Advanced data visualization

## Future Improvements
- Add predictive analytics for sales forecasting
- Implement interactive dashboards
- Include profit margin analysis
- Add customer segmentation analysis
- Include inventory turnover analysis
