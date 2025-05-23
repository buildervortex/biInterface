import plotly.graph_objects as go
from repository.biDashboardRepository import BiDashboardRepository


def IncomeProfit(repository: BiDashboardRepository):
    data = repository.getEmptySellingIncomeProfit()
    cylinder_names = [x[0] for x in data]
    selling_income = [x[1] for x in data]
    selling_profit = [x[2] for x in data]

    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=cylinder_names,
        y=selling_income,
        name="selling Income",
        marker_color='green'
    ))
    fig.add_trace(go.Bar(
        x=cylinder_names,
        y=selling_profit,
        name="selling Profit",
        marker_color='yellow'
    ))
    fig.update_layout(barmode='group', xaxis_tickangle=-45, barcornerradius=15)
    return fig
