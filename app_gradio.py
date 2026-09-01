import os
import gradio as gr
import pandas as pd
import matplotlib.pyplot as plt


# =========================
# LOAD DATASET
# =========================

df = pd.read_csv("Nassau Candy Distributor.csv")


# =========================
# ANALYSIS FUNCTION
# =========================

def show_analysis():

    # Basic calculations
    total_sales = df["Sales"].sum()
    total_profit = df["Gross Profit"].sum()
    total_cost = df["Cost"].sum()

    average_sales = df["Sales"].mean()
    average_profit = df["Gross Profit"].mean()

    # Profit margin
    df["Profit Margin"] = (df["Gross Profit"] / df["Sales"]) * 100

    average_margin = df["Profit Margin"].mean()

    # Product-wise calculations
    sales_by_product = (
        df.groupby("Product Name")["Sales"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    profit_by_product = (
        df.groupby("Product Name")["Gross Profit"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    cost_by_product = (
        df.groupby("Product Name")["Cost"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    margin_by_product = (
        df.groupby("Product Name")["Profit Margin"]
        .mean()
        .sort_values(ascending=False)
        .head(10)
    )

    # Highest products
    highest_sales_product = (
        df.groupby("Product Name")["Sales"]
        .sum()
        .idxmax()
    )

    highest_profit_product = (
        df.groupby("Product Name")["Gross Profit"]
        .sum()
        .idxmax()
    )

    highest_cost_product = (
        df.groupby("Product Name")["Cost"]
        .sum()
        .idxmax()
    )

    highest_margin_product = (
        df.groupby("Product Name")["Profit Margin"]
        .mean()
        .idxmax()
    )


    # =========================
    # BUSINESS SUMMARY
    # =========================

    summary = f"""
# 🍫 Nassau Candy Distributor — Business Dashboard

## 💰 Financial Overview

| Metric | Value |
|---|---:|
| **Total Sales** | ${total_sales:,.2f} |
| **Total Gross Profit** | ${total_profit:,.2f} |
| **Total Cost** | ${total_cost:,.2f} |
| **Average Sales** | ${average_sales:,.2f} |
| **Average Gross Profit** | ${average_profit:,.2f} |
| **Average Profit Margin** | {average_margin:.2f}% |

---

## 🏆 Key Business Insights

### 🥇 Highest Sales Product
**{highest_sales_product}**

### 💰 Highest Gross Profit Product
**{highest_profit_product}**

### 💸 Highest Cost Product
**{highest_cost_product}**

### 📈 Best Profit Margin Product
**{highest_margin_product}**

---

## 📊 Analysis Included

- Top 10 Products by Sales
- Top 10 Products by Gross Profit
- Top 10 Products by Cost
- Sales vs Gross Profit
- Sales vs Cost
- Top 10 Products by Profit Margin

"""

    # =========================
    # GRAPH 1 — SALES
    # =========================

    fig1, ax1 = plt.subplots(figsize=(10, 6))

    sales_by_product.sort_values().plot(
        kind="barh",
        ax=ax1
    )

    ax1.set_title("Top 10 Products by Sales")
    ax1.set_xlabel("Total Sales")
    ax1.set_ylabel("Product Name")

    plt.tight_layout()


    # =========================
    # GRAPH 2 — GROSS PROFIT
    # =========================

    fig2, ax2 = plt.subplots(figsize=(10, 6))

    profit_by_product.sort_values().plot(
        kind="barh",
        ax=ax2
    )

    ax2.set_title("Top 10 Products by Gross Profit")
    ax2.set_xlabel("Gross Profit")
    ax2.set_ylabel("Product Name")

    plt.tight_layout()


    # =========================
    # GRAPH 3 — COST
    # =========================

    fig3, ax3 = plt.subplots(figsize=(10, 6))

    cost_by_product.sort_values().plot(
        kind="barh",
        ax=ax3
    )

    ax3.set_title("Top 10 Products by Cost")
    ax3.set_xlabel("Total Cost")
    ax3.set_ylabel("Product Name")

    plt.tight_layout()


    # =========================
    # GRAPH 4 — SALES VS PROFIT
    # =========================

    comparison_profit = (
        df.groupby("Product Name")[["Sales", "Gross Profit"]]
        .sum()
        .sort_values("Sales", ascending=False)
        .head(10)
    )

    fig4, ax4 = plt.subplots(figsize=(10, 6))

    comparison_profit.plot(
        kind="bar",
        ax=ax4
    )

    ax4.set_title("Top 10 Products — Sales vs Gross Profit")
    ax4.set_xlabel("Product Name")
    ax4.set_ylabel("Amount")
    ax4.tick_params(axis="x", rotation=45)

    plt.tight_layout()


    # =========================
    # GRAPH 5 — SALES VS COST
    # =========================

    comparison_cost = (
        df.groupby("Product Name")[["Sales", "Cost"]]
        .sum()
        .sort_values("Sales", ascending=False)
        .head(10)
    )

    fig5, ax5 = plt.subplots(figsize=(10, 6))

    comparison_cost.plot(
        kind="bar",
        ax=ax5
    )

    ax5.set_title("Top 10 Products — Sales vs Cost")
    ax5.set_xlabel("Product Name")
    ax5.set_ylabel("Amount")
    ax5.tick_params(axis="x", rotation=45)

    plt.tight_layout()


    # =========================
    # GRAPH 6 — PROFIT MARGIN
    # =========================

    fig6, ax6 = plt.subplots(figsize=(10, 6))

    margin_by_product.sort_values().plot(
        kind="barh",
        ax=ax6
    )

    ax6.set_title("Top 10 Products by Profit Margin")
    ax6.set_xlabel("Profit Margin (%)")
    ax6.set_ylabel("Product Name")

    plt.tight_layout()


    return (
        summary,
        fig1,
        fig2,
        fig3,
        fig4,
        fig5,
        fig6
    )


# =========================
# GRADIO APP
# =========================

with gr.Blocks(title="Nassau Candy Distributor Dashboard") as app:

    gr.Markdown(
        """
        # 🍫 Nassau Candy Distributor
        ## 📊 Product Line Profitability & Margin Performance Dashboard

        **Analyze sales, costs, gross profit and profit margins across products.**
        """
    )

    generate_button = gr.Button(
        "🚀 Generate Complete Analysis",
        variant="primary"
    )

    output_summary = gr.Markdown()

    gr.Markdown("## 📈 Sales Analysis")

    sales_plot = gr.Plot()

    gr.Markdown("## 💰 Gross Profit Analysis")

    profit_plot = gr.Plot()

    gr.Markdown("## 💸 Cost Analysis")

    cost_plot = gr.Plot()

    gr.Markdown("## ⚖️ Sales vs Gross Profit")

    sales_profit_plot = gr.Plot()

    gr.Markdown("## 📊 Sales vs Cost")

    sales_cost_plot = gr.Plot()

    gr.Markdown("## 📈 Profit Margin Analysis")

    margin_plot = gr.Plot()


    generate_button.click(
        fn=show_analysis,
        inputs=[],
        outputs=[
            output_summary,
            sales_plot,
            profit_plot,
            cost_plot,
            sales_profit_plot,
            sales_cost_plot,
            margin_plot
        ]
    )


# =========================
# START APP
# =========================

app.launch(
    server_name="0.0.0.0",
    server_port=int(os.environ.get("PORT", 7861))
)
