import gradio as gr
import pandas as pd

df = pd.read_csv("Nassau Candy Distributor.csv")

def show_analysis():
    total_sales = df["Sales"].sum()
    total_profit = df["Gross Profit"].sum()
    total_cost = df["Cost"].sum()

    return (
        f"Total Sales: ${total_sales:,.2f}\n"
        f"Total Gross Profit: ${total_profit:,.2f}\n"
        f"Total Cost: ${total_cost:,.2f}"
    )

app = gr.Interface(
    fn=show_analysis,
    inputs=[],
    outputs="text",
    title="Nassau Candy Distributor Analysis",
    description="Product sales, cost and gross profit analysis."
)

app.launch(share=True)