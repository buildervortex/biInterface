import plotly.graph_objects as go
from repository.biDashboardRepository import BiDashboardRepository


def EmptySellingIncomeFigure(repository: BiDashboardRepository):
    data = repository.getEmptySellingIncomeProfit()
    cylinderName = [x[0] for x in data]
    income = [x[1] for x in data]
    profit = [x[2] for x in data]

    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=cylinderName,
        y=income,
        name="empty cylinder income",
        marker_color='orange'
    ))
    fig.add_trace(go.Bar(
        x=cylinderName,
        y=profit,
        name="empty cylinder profit",
        marker_color='blue'
    ))
    fig.update_layout(barmode='group', xaxis_tickangle=-45)
    return fig
