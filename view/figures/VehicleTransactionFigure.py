import plotly.graph_objects as go
from repository.biDashboardRepository import BiDashboardRepository

def VehicleTransactionFigure(repository: BiDashboardRepository):
    data = repository.getVehicleTransactionCounts()
    vehicle_number = data[0]
    transaction_count = data[1]

    # Correct data for Pie chart
    labels = ['Unfinished Loans', 'Finished Loans']
    values = [vehicle_number, transaction_count]

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
