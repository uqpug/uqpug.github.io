from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc

df = pd.read_csv("datasets/Players2024.csv")

df = df[df["positions"] != "Missing"]
df = df[df["height_cm"] > 100]

app = Dash()

app.layout = [
    html.Div(children="Players2024.csv data"),
    dash_table.DataTable(data=df.to_dict("records"), page_size=10),
    dcc.RadioItems(options=df["positions"].unique(), value="Attack", id="radio_button"),
    dcc.Graph(figure={}, id="graph"),
]


@callback(
    Output(component_id="graph", component_property="figure"),
    Input(component_id="radio_button", component_property="value"),
)
def update_graph(position_chosen):
    position = df[df["positions"] == position_chosen]
    fig = px.scatter(position, "age", "height_cm", range_y=[150, 210])
    return fig


if __name__ == "__main__":
    app.run(debug=True)
