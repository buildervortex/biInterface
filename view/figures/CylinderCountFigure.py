# import plotly.graph_objects as go
# from repository.biDashboardRepository import BiDashboardRepository

# def CylinderCountFigure(repository: BiDashboardRepository):
#     data = repository.getCylinderCountFromUserToGiveUs()
#     counter = data
    

#     # Correct data for Pie chart
#     labels = ['Cylinder Count From User To Give Us']
#     values = [ counter]

#     # Pull each slice slightly out
#     pull = [0.1, 0.1]

#     fig = go.Figure(data=[go.Pie(
#         labels=labels,
#         values=values,
#         pull=pull,
#         marker=dict(line=dict(color='white', width=8)),
#         textinfo='label+value',
#         hole=0  # Set to 0.4 if you want a donut chart
#     )])

#     fig.update_layout(
#         height=600,
#         width=600
#     )

#     return fig


import plotly.graph_objects as go
from repository.biDashboardRepository import BiDashboardRepository

def CylinderCountFigure(repository: BiDashboardRepository):
    data = repository.getCylinderCountFromUserToGiveUs()
    counter = data
    
    labels = ['Cylinder Count From User To Give Us']
    values = [counter]

    # Pull each slice slightly out (only one slice here, so one value)
    pull = [0.1]

    fig = go.Figure(data=[go.Pie(
        labels=labels,
        values=values,
        pull=pull,
        marker=dict(line=dict(color='white', width=8)),
        textinfo='label+value',
        hole=0  # 0 for pie chart, >0 for donut chart
    )])

    fig.update_layout(
        height=600,
        width=600
    )

    # To display the figure immediately (if running interactively)
    # fig.show()

    # To return the figure object for later use
    return fig
