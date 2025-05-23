import plotly.graph_objects as go
from repository.biDashboardRepository import BiDashboardRepository

def LoanFigure(repository: BiDashboardRepository):
    data = repository.getLoanFinishedUnfinishedCount("2024-05-15")
    unfinished_count = data[0]
    finished_count = data[1]

    # Correct data for Pie chart
    labels = ['Unfinished Loans', 'Finished Loans']
    values = [unfinished_count, finished_count]

    # Pull each slice slightly out
    pull = [0.1, 0.1]

    fig = go.Figure(data=[go.Pie(
        labels=labels,
        values=values,
        pull=pull,
        marker=dict(line=dict(color='white', width=2)),
        textinfo='label+percent+value',
        hole=0  # Set to 0.4 if you want a donut chart
    )])

    fig.update_layout(
        height=600,
        width=600
    )

    return fig
