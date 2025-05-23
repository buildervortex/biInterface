import plotly.graph_objects as go
from repository.biDashboardRepository import BiDashboardRepository

def SystemUsersHandledTransactionCount(repository: BiDashboardRepository):
    data = repository.getSystemUsersHandledTransactionCount()
    user_id = data[0]
    user_name = data[1]
    transaction_count = data[1]

    # Correct data for Pie chart
    labels = ['Unfinished Loans', 'Finished Loans','Finished Loans']
    values = [user_id, user_name,transaction_count]

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
