import plotly.graph_objects as go
from repository.biDashboardRepository import BiDashboardRepository


def GetManagerTransactionFigure(repository: BiDashboardRepository):
    data = repository.getEachManagerTransactionCount()
    user_name = [x[0] for x in data]
    transaction_count = [x[1] for x in data]
 

    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=user_name,
        y=transaction_count,
        name="Each Manager Transaction",
        marker_color='purple'
    ))
   
    fig.update_layout(barmode='group', xaxis_tickangle=-45)
    return fig
