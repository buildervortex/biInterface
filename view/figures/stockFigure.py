import plotly.graph_objects as go
from repository.biDashboardRepository import BiDashboardRepository


def stockFigure(repository: BiDashboardRepository):
    data = repository.getStock(1)
    cylinder_names = [x[0] for x in data]
    empty_count = [x[1] for x in data]
    filled_count = [x[2] for x in data]

    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=cylinder_names,
        y=empty_count,
        name="empty cylinder count",
        marker_color='indianred'
    ))
    fig.add_trace(go.Bar(
        x=cylinder_names,
        y=filled_count,
        name="filled cylinder count",
        marker_color='lightsalmon'
    ))
    fig.update_layout(barmode='group', xaxis_tickangle=-45)
    return fig
