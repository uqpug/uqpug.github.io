from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import seaborn as sns
import plotly.express as px

df = pd.read_csv("datasets/Players2024.csv")

app = Dash()

app.layout = [
    html.Div(children="Players 2024.csv data"),
    dcc.RadioItems(options=df["positions"].unique(), value="Attack", id="radio_button"),
    dash_table.DataTable(data=df.to_dict("records"), page_size=10, id="table"),
    dcc.Graph(figure=sns.relplot(df, x="age", y="height_cm")),
]


@callback(
    Output(component_id="table", component_property="data"),
    Input(component_id="radio_button", component_property="value"),
)
def update_table(position_chosen):
    return df[df["positions"] == position_chosen].to_dict("records")


app.run(debug=True)
