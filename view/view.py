from database.db import Database
from repository.biDashboardRepository import BiDashboardRepository
import dash
from dash import dcc, html
import plotly.graph_objects as go

from .figures.stockFigure import stockFigure


class MainLayout:
    def __init__(self, repo: BiDashboardRepository):
        self.repository = repo
        self.app = dash.Dash(__name__)
        self.server = self.app.server

        self.setLayout()
        pass

    def setLayout(self):
        self.app.layout = html.Div([
            html.H2("Monthly Gas Comparison"),
            dcc.Graph(id='bar-chart', figure=stockFigure(repository=self.repository))
        ])

    def run(self):
        self.app.run(debug=True)


class UI:
    def __init__(self, repo: BiDashboardRepository):
        self.repository = repo
        self.mainLayout = MainLayout(repo=self.repository)
        print("ui initialized")

    def run(self):
        self.mainLayout.run()
