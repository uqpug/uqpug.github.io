from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc

df = pd.read_csv("datasets/Players2024.csv")

df = df[df["positions"] != "Missing"]
df = df[df["height_cm"] > 100]

app = Dash()

external_stylesheets = [dbc.themes.CERULEAN]
app = Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = dbc.Container(
    [
        dbc.Row(
            [
                html.Div(children="Players2024.csv data"),
            ]
        ),
        dbc.Row(
            [
                dbc.RadioItems(
                    options=df["positions"].unique(), value="Attack", id="radio_button"
                ),
            ]
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        dash_table.DataTable(
                            data=None,
                            page_size=10,
                            style_table={"overflowX": "auto"},
                            id="table",
                        ),
                    ],
                    width=6,
                ),
                dbc.Col(
                    [
                        dcc.Graph(figure={}, id="graph"),
                    ],
                    width=6,
                ),
            ]
        ),
    ],
    fluid=True,
)


# Build in the callback(s)
@callback(
    Output(component_id="graph", component_property="figure"),
    Input(component_id="radio_button", component_property="value"),
)
def update_graph(position_chosen):
    position = df[df["positions"] == position_chosen]
    fig = px.scatter(position, "age", "height_cm", range_y=[150, 210])
    return fig


@callback(
    Output(component_id="table", component_property="data"),
    Input(component_id="radio_button", component_property="value"),
)
def update_table(position_chosen):
    return df[df["positions"] == position_chosen].to_dict("records")


if __name__ == "__main__":
    app.run(debug=True)
