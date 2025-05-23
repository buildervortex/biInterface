import dash
from dash import dcc, html
from repository.biDashboardRepository import BiDashboardRepository
from .figures.stockFigure import stockFigure
from .figures.IncomeFigure import create_income_dashboard
from .figures.cylinders_soldFigure import get_cylinder_sales_figure
from .figures.gas_sellingFigure import create_gas_sales_chart
from .figures.gas_priceFigure import gas_price
from .figures.empty_and_filledFigure import get_cylinder_status_figure
from .figures.get_blacklist_dataFigure import get_blacklist_data
from .figures.one_gas_priceFigure import one_gas_price
from .figures.empty_cylinderFigure import show_empty_cylinder_stock_figure


def mainLayout(repo: BiDashboardRepository):
    return html.Div([
          
        html.Div(


        html.H2("Monthly Gas Comparison"),
        dcc.Graph(id='bar-chart', figure=stockFigure(repository=repo)),

          ),

       html.Div(
           
            html.H1("Income Dashboard Example", style={'textAlign': 'center'}),
            dcc.Graph(id='',figure=create_income_dashboard(repository=repo))    

       ),


       html.Div(
            html.H2("Shell Gas Cylinder Sales", style={'textAlign': 'center'}),
           
           dcc.Graph(id='',figure=get_cylinder_sales_figure(repository=repo))
           
       ),


        html.Div(
            html.H2("Shell Gas Cylinder Sales", style={'textAlign': 'center'}),
           dcc.Graph(id='',figure=create_gas_sales_chart(repository=repo))
           
       )


       
    ])
    pass
