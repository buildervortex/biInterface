from database.db import Database
from repository.biDashboardRepository import BiDashboardRepository
import dash
from dash import dcc, html
import plotly.graph_objects as go

from .figures.stockFigure import stockFigure
from .mainLayout import mainLayout


class MainLayout:
    def __init__(self, repo: BiDashboardRepository):
        self.repository = repo
        self.app = dash.Dash(__name__)
        self.server = self.app.server

        self.setLayout()
        pass

    def setLayout(self):
        self.app.layout = mainLayout(self.repository)

    def run(self):
        self.app.run(debug=True)


class UI:
    def __init__(self, repo: BiDashboardRepository):
        self.repository = repo
        self.mainLayout = MainLayout(repo=self.repository)
        print("ui initialized")

    def run(self):
        self.mainLayout.run()
