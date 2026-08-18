import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Nassau Candy Distributor.csv")

print("Dataset successfully loaded!")
print(df.head())
print(df.shape)
print(df.columns)
print(df.info())
print(df.describe())
print(df.isnull().sum())
print(df.duplicated().sum())
print(df.dtypes)
print(df.nunique())

print("Total Sales:", df["Sales"].sum())
print("Total Gross Profit:", df["Gross Profit"].sum())
print("Total Cost:", df["Cost"].sum())

print(df["Product Name"].value_counts().head(10))
print(df.groupby("Product Name")["Sales"].sum().sort_values(ascending=False).head(10))
print(df.groupby("Product Name")["Gross Profit"].sum().sort_values(ascending=False).head(10))

print("Average Sales:", df["Sales"].mean())
print("Maximum Sales:", df["Sales"].max())
print("Minimum Sales:", df["Sales"].min())

sales_by_product = df.groupby("Product Name")["Sales"].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(10, 6))
sales_by_product.plot(kind="bar")
plt.title("Top 10 Products by Sales")
plt.xlabel("Product Name")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

profit_by_product = df.groupby("Product Name")["Gross Profit"].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(10, 6))
profit_by_product.plot(kind="bar")
plt.title("Top 10 Products by Gross Profit")
plt.xlabel("Product Name")
plt.ylabel("Gross Profit")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

comparison = df.groupby("Product Name")[["Sales", "Gross Profit"]].sum()
comparison = comparison.sort_values("Sales", ascending=False).head(10)

comparison.plot(kind="bar", figsize=(10, 6))
plt.title("Top 10 Products - Sales vs Gross Profit")
plt.xlabel("Product Name")
plt.ylabel("Amount")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

cost_by_product = df.groupby("Product Name")["Cost"].sum()
cost_by_product = cost_by_product.sort_values(ascending=False).head(10)

print("Top 10 Products by Cost:")
print(cost_by_product)

plt.figure(figsize=(10, 6))
cost_by_product.plot(kind="bar")
plt.title("Top 10 Products by Cost")
plt.xlabel("Product Name")
plt.ylabel("Total Cost")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

comparison = df.groupby("Product Name")[["Sales", "Cost"]].sum()
comparison = comparison.sort_values("Sales", ascending=False).head(10)

comparison.plot(kind="bar", figsize=(10, 6))
plt.title("Top 10 Products - Sales vs Cost")
plt.xlabel("Product Name")
plt.ylabel("Amount")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

df["Profit Margin"] = (df["Gross Profit"] / df["Sales"]) * 100

margin = df.groupby("Product Name")["Profit Margin"].mean()
margin = margin.sort_values(ascending=False).head(10)

print("\nTop 10 Products by Profit Margin:")
print(margin)

margin.plot(kind="bar", figsize=(10, 6))
plt.title("Top 10 Products by Profit Margin")
plt.xlabel("Product Name")
plt.ylabel("Profit Margin (%)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

print("\n========== BUSINESS SUMMARY ==========")

print("Total Sales:", df["Sales"].sum())
print("Total Cost:", df["Cost"].sum())
print("Total Gross Profit:", df["Gross Profit"].sum())
print("Average Sales:", df["Sales"].mean())
print("Average Gross Profit:", df["Gross Profit"].mean())
print("Average Profit Margin:", df["Profit Margin"].mean())

print("\n========== FINAL BUSINESS INSIGHTS ==========")

print("Highest Sales Product:")
print(df.groupby("Product Name")["Sales"].sum().idxmax())

print("\nHighest Gross Profit Product:")
print(df.groupby("Product Name")["Gross Profit"].sum().idxmax())

print("\nHighest Cost Product:")
print(df.groupby("Product Name")["Cost"].sum().idxmax())

print("\nBest Profit Margin Product:")
print(df.groupby("Product Name")["Profit Margin"].mean().idxmax())