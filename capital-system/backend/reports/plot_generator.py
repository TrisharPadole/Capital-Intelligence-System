import plotly.graph_objects as go
import plotly.io as pio
import os
from datetime import datetime


def generate_financial_plots(metrics: dict):
    os.makedirs("backend/generated_reports", exist_ok=True)

    fig = go.Figure()

    fig.add_trace(go.Bar(
        x=["Revenue", "EBITDA"],
        y=[metrics["monthly_revenue"], metrics["ebitda"]],
        name="Profitability"
    ))

    fig.add_trace(go.Bar(
        x=["DSCR", "Runway (months)"],
        y=[metrics["dscr"], metrics["runway"]],
        name="Liquidity"
    ))

    filename = f"financial_charts_{datetime.now().strftime('%Y%m%d_%H%M%S')}.html"
    filepath = os.path.join("backend/generated_reports", filename)

    pio.write_html(fig, filepath, auto_open=False)

    return filename
