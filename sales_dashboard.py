import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import seaborn as sns
import os

# Load the data
file_path  = "D:\Projects-git\SalesDashboard\sales_data.csv"

data = pd.read_csv(file_path,encoding='latin1')

#exploring data
print(data.head())

print(data.info())

print(data.describe())

#clean data set
print(data.isnull().sum())

if 'Sales' in data.columns:
    data['Sales'] = data['Sales'].fillna(data['Sales'].mean())
    
if 'Date' in data.columns:
    data['Date'] = pd.to_datetime(data['Date'])
    
    
    
#analysize the data
if 'Product' in data.columns and 'Sales' in data.columns:
    product_sales = data.groupby('Product')['Sales'].sum()
    print("\n Total Sales By Product:")
    print(product_sales)
    
if 'Date' in data.columns and 'Sales' in data.columns:
    data['Month'] = data['Date'].dt.to_period('M')
    monthly_sales = data.groupby('Month')['Sales'].sum()
    print("\nMonthly Sales Trends:")
    print(monthly_sales)
    
#visualize the data

if 'Product' in data.columns and 'Sales' in data.columns:
    product_sales.plot(kind = 'bar',figsize=(10,6), color='skyblue')
    plt.title('Total Sales By Product')
    plt.xlabel('Product')
    plt.ylabel('Total Sales')
    plt.xticks(rotation=45)
    plt.show()
    
    
if 'Month' in data.columns and 'Sales' in data.columns:
    monthly_sales.plot(kind='line', marker='o', figsize=(10, 6), color='green')
    plt.title("Monthly Sales Trends")
    plt.xlabel("Month")
    plt.ylabel("Total Sales")
    plt.grid()
    plt.show()
    plt.savefig('monthly_sales.png')
    
if 'Sales' in data.columns:
    data['Sales'].plot(kind='hist', bins=20, figsize=(10, 6), color='orange')
    plt.title("Distribution of Sales")
    plt.xlabel("Sales")
    plt.ylabel("Frequency")
    plt.show()
    plt.savefig('sales_distribution.png')


print("\nAnalysis Complete. Visualizations generated. Interpret the trends to gain insights!")