import plotly.graph_objects as go
from repository.biDashboardRepository import BiDashboardRepository

def displayCylinderCountCard(repo) -> go.Figure:
    count = repo.getCylinderCountFromUserToGiveUs()  # Use 'repo' here

    fig = go.Figure()

    fig.add_trace(go.Indicator(
        mode="number",
        value=count,
        title={"text": "Cylinder Count From User To Give Us"},
        number={"font": {"size": 48}}
    ))

    fig.update_layout(
        height=200,
        margin=dict(t=20, b=20, l=20, r=20),
        paper_bgcolor="white"
    )

    return fig
