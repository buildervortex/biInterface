import plotly.graph_objects as go
from repository.biDashboardRepository import BiDashboardRepository

def CylinderCountFigure(repository: BiDashboardRepository):
    counter = repository.getCylinderCountFromUserToGiveUs()

    # Ensure counter is a single number (int or float)
    if not isinstance(counter, (int, float)):
        raise ValueError("Expected a single numeric value from getCylinderCountFromUserToGiveUs()")

    labels = ['Cylinders to Return']
    values = [counter]

    fig = go.Figure(data=[go.Pie(
        labels=labels,
        values=values,
        pull=[0.1],  # only one value, so one pull
        marker=dict(line=dict(color='white', width=4)),
        textinfo='label+value',
        hole=0
    )])

    fig.update_layout(
        height=400,
        width=400
    )

    return fig
