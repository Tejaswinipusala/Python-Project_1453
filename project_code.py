# Import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
file_path = "amazon_products_sales_data_cleaned.csv"   # Change path if needed
df = pd.read_csv(file_path)

# -----------------------
# Data Cleaning
# -----------------------
df_cleaned = df.copy()
df_cleaned['product_rating'] = df_cleaned['product_rating'].fillna(df_cleaned['product_rating'].mean())
df_cleaned['discounted_price'] = df_cleaned['discounted_price'].fillna(df_cleaned['discounted_price'].mean())
df_cleaned['discount_percentage'] = df_cleaned['discount_percentage'].fillna(0)

# -----------------------
# Analysis & Visualization
# -----------------------

# 1. Distribution of product ratings
plt.figure(figsize=(6,4))
plt.hist(df_cleaned['product_rating'], bins=20, color='skyblue', edgecolor='black')
plt.title("Distribution of Product Ratings")
plt.xlabel("Rating")
plt.ylabel("Number of Products")
plt.show()

# 2. Top 10 categories by number of products
top_categories = df_cleaned['product_category'].value_counts().head(10)
plt.figure(figsize=(6,4))
top_categories.plot(kind='bar', color='orange', edgecolor='black')
plt.title("Top 10 Product Categories by Count")
plt.xlabel("Number of Products")
plt.ylabel("Category")
plt.xticks(rotation=45)
plt.show()

# 3. Average discount percentage per category (Top 10)
avg_discount = df_cleaned.groupby('product_category')['discount_percentage'].mean().sort_values(ascending=False).head(10)
plt.figure(figsize=(8,4))
avg_discount.plot(kind='bar', color='green', edgecolor='black')
plt.title("Top 10 Categories by Average Discount %")
plt.xlabel("Category")
plt.ylabel("Average Discount %")
plt.xticks(rotation=45)
plt.show()

# 4. Relationship between discount percentage and rating (scatter)
plt.figure(figsize=(6,4))
plt.scatter(df_cleaned['discount_percentage'], df_cleaned['product_rating'], alpha=0.3, color='purple')
plt.title("Discount % vs Product Rating")
plt.xlabel("Discount Percentage")
plt.ylabel("Rating")
plt.show()


