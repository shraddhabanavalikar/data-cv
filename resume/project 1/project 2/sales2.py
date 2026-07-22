import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("sales.csv")

# Convert Date
df['Date'] = pd.to_datetime(df['Date'])

# Create subplots (dashboard style)
fig, axes = plt.subplots(2, 2, figsize=(12, 8))

# 1️⃣ Sales by Region
region_sales = df.groupby("Region")["Sales"].sum()
axes[0, 0].bar(region_sales.index, region_sales.values)
axes[0, 0].set_title("Sales by Region")

# 2️⃣ Sales by Category
category_sales = df.groupby("Category")["Sales"].sum()
axes[0, 1].pie(category_sales.values, labels=category_sales.index, autopct='%1.1f%%')
axes[0, 1].set_title("Sales by Category")

# 3️⃣ Monthly Sales Trend
monthly_sales = df.groupby(df['Date'].dt.month)["Sales"].sum()
axes[1, 0].plot(monthly_sales.index, monthly_sales.values, marker='o')
axes[1, 0].set_title("Monthly Sales Trend")

# 4️⃣ Profit by Region
region_profit = df.groupby("Region")["Profit"].sum()
axes[1, 1].bar(region_profit.index, region_profit.values)
axes[1, 1].set_title("Profit by Region")

# Layout
plt.tight_layout()
plt.show()