# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc, Output, Input
import plotly.express as px
import pandas as pd
#nitialize dash
app = Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
#read data
df = pd.read_csv("Final_sales.csv")
df0 = df.sort_values(by= "date")

COLORS={'primary':'#FEDBFF',
        'secondary':'#D598EB',
        'font':'#522A61'}

#create visualization
def generate_figure(chart_data):
    fig = px.line(chart_data, x="date", y="sales", title="Pink Morsel Sales")
    fig.update_layout(plot_bgcolor=COLORS['secondary'],
        paper_bgcolor=COLORS['primary'],
        font_color=COLORS["font"])
    return fig

visualization= dcc.Graph(
    id="visualization",
    figure=generate_figure(df0)    )

#create the header
header= html.H1(
    "Pink Morsel Visualizer",
    id="header",
    style={
        "background-color": COLORS["secondary"],
        "color": COLORS["font"],
        "border-radius": "20px"
    }
)

#region picker
region_picker= dcc.RadioItems(
    ["north", "east", "south", "west", "all"],
    "north",
    id= "region_picker",
    inline=True

)

region_picker_wrapper= html.Div(
    [region_picker],
    style= {"font-size": "150%"}
)

#define the region picker callback
@app.callback(
    Output(visualization, "figure"),
    Input(region_picker, "value")
)
def update_graph(region):
    #filter the dataset
    if region == "all":
        trimmed_data= df0
    else:
        trimmed_data= df0[df0["region"] == region]

    #generate a new line chart with filtered data
    figure = generate_figure(trimmed_data)
    return figure
#define app layout
app.layout= html.Div(
    [header,
    visualization,
    region_picker_wrapper],
    style={"textAlign": "center",
        "background-color": COLORS["primary"],
        "border-radius": "20px"}
)


if __name__ == '__main__':
    app.run_server(debug=True)

