import dash
from dash import dcc, html
from repository.biDashboardRepository import BiDashboardRepository
from .figures.stockFigure import stockFigure
from .figures.loanFigure import LoanFigure
from .figures.GasIncomesFigure import GasIncomesFigure
from .figures.IncomeFigure import IncomeProfit
from .figures.ManagerTransactionFigure import GetManagerTransactionFigure
from .figures.EmptySellingIncomeFigure import EmptySellingIncomeFigure
from .figures.VehicleTransactionFigure import VehicleTransactionFigure
from .figures.UnFinishedLoanBalanceFigure import UnFinishedLoanBalanceFigure
from .figures.CylinderSellCountFigure import CylinderSellCountFigure
from .figures.reg_and_unregFigure import RegAndUnregCustomerCountsFigure
from .figures.CylinderCountFigure import displayCylinderCountCard

def mainLayout(repo: BiDashboardRepository):
    return html.Div(
        style={
            'display': 'grid',
            'gridTemplateColumns': 'repeat(auto-fit, minmax(500px, 1fr))',
            'gap': '20px',
            'padding': '20px',
            'minHeight': '100vh',
            'backgroundColor': '#f5f5f5'
        },
        children=[
            
            
            html.Div([
                html.H2("Cylinder Inventory"),
                dcc.Graph(figure=displayCylinderCountCard(repo)),

            ] ),




            html.Div([
                html.H2("Monthly Gas Comparison"),
                dcc.Graph(figure=stockFigure(repository=repo)),
            ], style={'backgroundColor': 'white', 'padding': '15px', 'borderRadius': '8px'}),

            html.Div([
                html.H2("Loan Details"),
                dcc.Graph(figure=LoanFigure(repository=repo)),
            ], style={'backgroundColor': 'white', 'padding': '15px', 'borderRadius': '8px'}),

            html.Div([
                html.H2("Gas Income Details"),
                dcc.Graph(figure=GasIncomesFigure(repository=repo)),
            ], style={'backgroundColor': 'white', 'padding': '15px', 'borderRadius': '8px'}),

            html.Div([
                html.H2("Total Profit"),
                dcc.Graph(figure=IncomeProfit(repository=repo)),
            ], style={'backgroundColor': 'white', 'padding': '15px', 'borderRadius': '8px'}),

            html.Div([
                html.H2("Manager Transactions"),
                dcc.Graph(figure=GetManagerTransactionFigure(repository=repo)),
            ], style={'backgroundColor': 'white', 'padding': '15px', 'borderRadius': '8px'}),

            html.Div([
                html.H2("Empty Cylinder Sales Income"),
                dcc.Graph(figure=EmptySellingIncomeFigure(repository=repo)),
            ], style={'backgroundColor': 'white', 'padding': '15px', 'borderRadius': '8px'}),

            html.Div([
                html.H2("Vehicle Transactions"),
                dcc.Graph(figure=VehicleTransactionFigure(repository=repo)),
            ], style={'backgroundColor': 'white', 'padding': '15px', 'borderRadius': '8px'}),

            html.Div([
                html.H2("Unfinished Loan Balance"),
                dcc.Graph(figure=UnFinishedLoanBalanceFigure(repository=repo)),
            ], style={'backgroundColor': 'white', 'padding': '15px', 'borderRadius': '8px'}),

            html.Div([
                html.H2("Cylinder Sell Count"),
                dcc.Graph(figure=CylinderSellCountFigure(repository=repo)),
            ], style={'backgroundColor': 'white', 'padding': '15px', 'borderRadius': '8px'}),

            html.Div([
                html.H2("Customer Registration Stats"),
                dcc.Graph(figure=RegAndUnregCustomerCountsFigure(repository=repo)),
            ], style={'backgroundColor': 'white', 'padding': '15px', 'borderRadius': '8px'}),

        ]
    )
