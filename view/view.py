from database.db import Database
from repository.biDashboardRepository import BiDashboardRepository
import dash
from dash import dcc, html
import plotly.graph_objects as go


# app = dash.Dash(__name__)
# server = app.server

# # Data
# months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
#           'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

# fig = go.Figure()
# fig.add_trace(go.Bar(
#     x=months,
#     y=[20, 14, 25, 16, 18, 22, 19, 15, 12, 16, 14, 17],
#     name='filled cylinder',
#     marker_color='indianred'
# ))
# fig.add_trace(go.Bar(
#     x=months,
#     y=[19, 14, 22, 14, 16, 19, 15, 14, 10, 12, 12, 16],
#     name='empty cylinder',
#     marker_color='lightsalmon'
# ))
# fig.update_layout(barmode='group', xaxis_tickangle=-45)

# # Layout
# app.layout = html.Div([
#     html.H2("Monthly Gas Comparison"),
#     dcc.Graph(id='bar-chart', figure=fig)
# ])


class MainLayout:
    def __init__(self, repo: BiDashboardRepository):
        self.repository = repo
        self.app = dash.Dash(__name__)
        self.server = self.app.server

        self.setLayout()
        pass

    def stockFigure(self):
        data = self.repository.getStock(1)
        cylinder_names = [x[0] for x in data]
        empty_count = [x[1] for x in data]
        filled_count = [x[2] for x in data]

        fig = go.Figure()
        fig.add_trace(go.Bar(
            x=cylinder_names,
            y=empty_count,
            name="empty cylinder count",
            marker_color='indianred'
        ))
        fig.add_trace(go.Bar(
            x=cylinder_names,
            y=filled_count,
            name="filled cylinder count",
            marker_color='lightsalmon'
        ))
        fig.update_layout(barmode='group', xaxis_tickangle=-45)
        return fig

    def setLayout(self):
        self.app.layout = html.Div([
            html.H2("Monthly Gas Comparison"),
            dcc.Graph(id='bar-chart', figure=self.stockFigure())
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
