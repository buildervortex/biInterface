import plotly.graph_objects as go
from repository.biDashboardRepository import BiDashboardRepository

def VehicleTransactionFigure(repository: BiDashboardRepository):
    data = repository.getVehicleTransactionCounts()

    if not data:
        return go.Figure()  # Return an empty figure if there's no data

    # Unzip the list of tuples
    vehicle_numbers, transaction_counts = zip(*data)

    fig = go.Figure(data=[go.Pie(
        labels=vehicle_numbers,
        values=transaction_counts,
        pull=[0.05] * len(vehicle_numbers),  # Slight pull for all slices
        marker=dict(line=dict(color='white', width=2)),
        textinfo='label+percent+value',
        hole=0  # Set to 0.4 if you want a donut chart
    )])

    fig.update_layout(
        title_text="Vehicle Transaction Distribution",
        height=600,
        width=600
    )

    return fig
