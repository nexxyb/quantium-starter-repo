# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.read_csv("Final_sales.csv")
df0 = df.sort_values(by= "date")

fig = px.line(df0, x="date", y="sales", color="region")

app.layout = html.Div(children=[
    html.H1(children="Soul's Food", style={'textAlign':'center'}),

    html.Div(children='''
        Pink Morsel Sales Analysis Dashboard.
    ''', style={'textAlign':'center'}),

    html.Br(),
    html.Label('Radio Items'),
    dcc.RadioItems(['North', 'South', 'East', 'West','All'], style={'padding':10, 'flex':1}),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)

