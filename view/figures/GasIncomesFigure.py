import plotly.graph_objects as go
from repository.biDashboardRepository import BiDashboardRepository


def GasIncomesFigure(repository: BiDashboardRepository):
    data = repository.getGasIncomes()
    cylinder_names = [x[0] for x in data]
    selling_income = [x[1] for x in data]
    selling_profit = [x[2] for x in data]

    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=cylinder_names,
        y=selling_income,
        name="selling Income",
        marker_color='blue'
    ))
    fig.add_trace(go.Bar(
        x=cylinder_names,
        y=selling_profit,
        name="selling Profit",
        marker_color='red'
    ))
    fig.update_layout(barmode='group', xaxis_tickangle=-45)
    return fig
