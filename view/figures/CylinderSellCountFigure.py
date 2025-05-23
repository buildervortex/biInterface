import plotly.express as px
import pandas as pd
from repository.biDashboardRepository import BiDashboardRepository


def CylinderSellCountFigure(repository: BiDashboardRepository):
    data = repository.getCylinderTypeBySellCount()
    display_name = [x[1] for x in data]
    total_given = [x[0] for x in data]

    df = pd.DataFrame({
        'number': total_given,
        'stage': display_name
    })

    fig = px.funnel(df, x='number', y='stage', height=600,
                    color_discrete_sequence=["#F08080", "#FA8072", "#FFA07A"])
    return fig
