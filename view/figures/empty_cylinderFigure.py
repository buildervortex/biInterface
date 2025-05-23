import plotly.express as px
from repository.biDashboardRepository import BiDashboardRepository


def show_empty_cylinder_stock_figure(repository: BiDashboardRepository):
     data = repository.getStock(1)
     empty_count = [x[1] for x in data]
     cylinder_names = [x[0] for x in data]

     data = dict(
        x=empty_count,
        y=cylinder_names,
          )
     fig = px.funnel(data, x='number', y='stage',height=600, color_discrete_sequence=["#F08080", "#FA8072", "#FFA07A"],)
     return fig




###############################################################

# def show_empty_cylinder_stock_figure():
#     data = dict(
#         number=[50, 30, 20],
#         stage=["12.5kg", "5kg", "2.5kg"]
#     )
#     fig = px.funnel(data, x='number', y='stage',height=600, color_discrete_sequence=["#F08080", "#FA8072", "#FFA07A"],)
#     return fig
