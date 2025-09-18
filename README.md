# 📊 Amazon Product Sales Data Analysis

This project analyzes the **Amazon Products Dataset** to uncover insights about product categories, ratings, discounts, and overall trends.  
Using Python libraries like **Pandas, NumPy, and Matplotlib**, the project performs **data cleaning, analysis, and visualization** to better understand customer preferences and sales strategies.

---

## 📂 Dataset

The dataset used in this project is publicly available on Kaggle:

🔗 [Amazon Products Dataset](https://www.kaggle.com/datasets/lokeshparab/amazon-products-dataset)

---

## 🛠️ Installation

Make sure you have **Python 3.8+** installed.  
Install the required libraries using pip:

```bash
pip install numpy pandas matplotlib

# -----------------------
# Key Insights Extraction
# -----------------------

# 1. Average product rating
avg_rating = df_cleaned['product_rating'].mean()

# 2. Top category by number of products
top_category = df_cleaned['product_category'].value_counts().idxmax()

# 3. Category with highest average discount
max_discount_category = df_cleaned.groupby('product_category')['discount_percentage'].mean().idxmax()

# 4. Correlation between discount % and rating
correlation = df_cleaned['discount_percentage'].corr(df_cleaned['product_rating'])

print("🔑 Key Insights:")
print(f"- Average Product Rating: {avg_rating:.2f}")
print(f"- Top Category by Number of Products: {top_category}")
print(f"- Category with Highest Average Discount: {max_discount_category}")
print(f"- Correlation between Discount % and Ratings: {correlation:.2f}")


