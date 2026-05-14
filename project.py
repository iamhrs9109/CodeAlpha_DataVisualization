import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("Data/Sample - Superstore.csv", encoding='latin1')

# Sales by Category
sales_by_category = df.groupby("Category")["Sales"].sum()

# Create chart
plt.figure(figsize=(8,5))

sns.barplot(
    x=sales_by_category.index,
    y=sales_by_category.values
)

plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")

# Save chart
plt.savefig("Image/sales_chart.png")

print("Chart Saved Successfully")

plt.savefig("Image/profit_chart.png")
plt.savefig("Image/heatmap.png")
plt.savefig("Image/monthly_sales.png")