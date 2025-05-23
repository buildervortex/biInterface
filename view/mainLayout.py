import dash
from dash import dcc, html
from repository.biDashboardRepository import BiDashboardRepository
from .figures.stockFigure import stockFigure
from .figures.cylinders_soldFigure import get_cylinder_sales_figure
from .figures.gas_sellingFigure import create_gas_sales_chart
from .figures.gas_priceFigure import gas_price
from .figures.get_blacklist_dataFigure import get_blacklist_data
from .figures.empty_cylinderFigure import show_empty_cylinder_stock_figure
from .figures.loanFigure import LoanFigure
from .figures.GasIncomesFigure import GasIncomesFigure
from .figures.IncomeFigure import IncomeProfit


def mainLayout(repo: BiDashboardRepository):
    return html.Div([
          
        html.Div([
            html.H2("Monthly Gas Comparison"),
            dcc.Graph(id='bar-chart', figure=stockFigure(repository=repo)),
        ]),

        html.Div([
            html.H2("Loan Details"),
            dcc.Graph(id='pie-chart', figure=LoanFigure(repository=repo)),
        ]),
        

        html.Div([
            html.H2("Income Deatails"),
            dcc.Graph(id='bar-chart2', figure=GasIncomesFigure(repository=repo)),
        ]),
        

          html.Div([
            html.H2("Income Deatails"),
            dcc.Graph(id='bar-chart3', figure=IncomeProfit(repository=repo)),
        ]),

        
        




    #    html.Div(
           
    #         html.H1("Income Dashboard Example", style={'textAlign': 'center'}),
    #         dcc.Graph(id='',figure=create_income_dashboard(repository=repo))    

    #    ),


    #    html.Div(
    #         html.H2("Shell Gas Cylinder Sales", style={'textAlign': 'center'}),
           
    #        dcc.Graph(id='',figure=get_cylinder_sales_figure(repository=repo))
           
    #    ),


    #     html.Div(
    #         html.H2("Shell Gas Cylinder Sales", style={'textAlign': 'center'}),
    #        dcc.Graph(id='',figure=create_gas_sales_chart(repository=repo))
           
    #    ),

       
    #     html.Div(
    #         html.H2("Shell Gas Cylinder Sales", style={'textAlign': 'center'}),
    #        dcc.Graph(id='',figure=show_empty_cylinder_stock_figure(repository=repo))
           
    #    )


       
    ])
    pass
