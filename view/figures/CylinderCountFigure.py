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
<<<<<<< HEAD
    counter = repository.getCylinderCountFromUserToGiveUs()

    # Ensure counter is a single number (int or float)
    if not isinstance(counter, (int, float)):
        raise ValueError("Expected a single numeric value from getCylinderCountFromUserToGiveUs()")

    labels = ['Cylinders to Return']
    values = [counter]
=======
    data = repository.getCylinderCountFromUserToGiveUs()
    counter = data
    
    labels = ['Cylinder Count From User To Give Us']
    values = [counter]

    # Pull each slice slightly out (only one slice here, so one value)
    pull = [0.1]
>>>>>>> af68710ce52140f2d131fe1f50848e401c6e952c

    fig = go.Figure(data=[go.Pie(
        labels=labels,
        values=values,
        pull=[0.1],  # only one value, so one pull
        marker=dict(line=dict(color='white', width=4)),
        textinfo='label+value',
<<<<<<< HEAD
        hole=0
=======
        hole=0  # 0 for pie chart, >0 for donut chart
>>>>>>> af68710ce52140f2d131fe1f50848e401c6e952c
    )])

    fig.update_layout(
        height=400,
        width=400
    )

    # To display the figure immediately (if running interactively)
    # fig.show()

    # To return the figure object for later use
    return fig
