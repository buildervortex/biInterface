import dash
from dash import dcc, html
import plotly.graph_objects as go

app = dash.Dash(__name__)
server = app.server  

# Data
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

fig = go.Figure()
fig.add_trace(go.Bar(
    x=months,
    y=[20, 14, 25, 16, 18, 22, 19, 15, 12, 16, 14, 17],
    name='filled cylinder',
    marker_color='indianred'
))
fig.add_trace(go.Bar(
    x=months,
    y=[19, 14, 22, 14, 16, 19, 15, 14, 10, 12, 12, 16],
    name='empty cylinder',
    marker_color='lightsalmon'
))
fig.update_layout(barmode='group', xaxis_tickangle=-45)

# Layout
app.layout = html.Div([
    html.H2("Monthly Gas Comparison"),
    dcc.Graph(id='bar-chart', figure=fig)
])

# 🔥 New correct way to run the server
if __name__ == '__main__':
    app.run(debug=True)
