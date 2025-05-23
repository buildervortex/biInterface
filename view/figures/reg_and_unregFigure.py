import plotly.graph_objects as go
from repository.biDashboardRepository import BiDashboardRepository

def RegAndUnregCustomerCountsFigure(repository: BiDashboardRepository):
    data = repository.getRegAndUnregCustomerCounts()

    # Extract counts from tuples
    registered_count = next((count for ctype, count in data if ctype == "registered"), 0)
    anonymous_count = next((count for ctype, count in data if ctype == "anonymous"), 0)

    # Labels and values for the pie chart
    labels = ['Registered Customers', 'Anonymous Customers']
    values = [registered_count, anonymous_count]
    pull = [0.1, 0.1]

    fig = go.Figure(data=[go.Pie(
        labels=labels,
        values=values,
        pull=pull,
        marker=dict(line=dict(color='white', width=2)),
        textinfo='label+percent+value',
        hole=0  # Set to 0.4 if you want a donut chart
    )])

    fig.update_layout(height=600, width=600)
    return fig
