import plotly.graph_objects as go
from repository.biDashboardRepository import BiDashboardRepository

def CylinderCountFigure(repository: BiDashboardRepository):
    data = repository.getCylinderCountFromUserToGiveUs()
    counter = data
    

    # Correct data for Pie chart
    labels = ['Cylinder Count From User To Give Us']
    values = [ counter]

    # Pull each slice slightly out
    pull = [0.1, 0.1]

    fig = go.Figure(data=[go.Pie(
        labels=labels,
        values=values,
        pull=pull,
        marker=dict(line=dict(color='white', width=8)),
        textinfo='label+value',
        hole=0  # Set to 0.4 if you want a donut chart
    )])

    fig.update_layout(
        height=600,
        width=600
    )

    return fig
