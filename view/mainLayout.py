import dash
from dash import dcc, html
from repository.biDashboardRepository import BiDashboardRepository
from .figures.stockFigure import stockFigure


def mainLayout(repo: BiDashboardRepository):
    return html.Div([
        html.H2("Monthly Gas Comparison"),
        dcc.Graph(id='bar-chart', figure=stockFigure(repository=repo)),

       html.Div()
     


    ])
    pass
