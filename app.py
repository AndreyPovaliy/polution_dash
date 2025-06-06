from dash import Dash
from layouts import create_layout
from callbacks import register_callbacks
import dash_bootstrap_components as dbc

app = Dash(external_stylesheets=[dbc.themes.SANDSTONE])
app.title = "Состояние чего-то другого"
server = app.server

app.layout = create_layout()

register_callbacks(app)

if __name__ == "__main__":
    app.run(debug=False)