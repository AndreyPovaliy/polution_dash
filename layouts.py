import dash_bootstrap_components as dbc
from dash import dcc

def create_layout():
    return dbc.Container([
        dbc.NavbarSimple(
            brand="Другая информация о погоде",
            brand_href="#",
            dark=True,
            className="mb-4"
        ),
        dbc.Row([
            dbc.Col(dbc.Card(id='weather-output', body=True), width=6, xs=12, md=6, className="mb-1"), 
            dbc.Col([dbc.Input(id = "city-input", type = "text", placeholder = "Введите город", value='Москва')], width = 6, xs = 12, md = 6, className="mb-2"),
            ], className="mb-3"), 
 
        dbc.Row([
            dbc.Col(dcc.Graph(id='wind_kph-graph'), width=4, xs=12, md=4, className="mb-2"),
            dbc.Col(dcc.Graph(id='pressure_mb-graph'), width=4, xs=12, md=4, className="mb-2"),
            dbc.Col(dcc.Graph(id='humidity-graph'), width=4, xs=12, md=4, className="mb-2"),
        ], className="mb-3"),
  
        dbc.Row([
            dbc.Col(dcc.Graph(id='cloud-graph'), width=4, xs=12, md=4, className="mb-2"),
            dbc.Col(dcc.Graph(id='uv-graph'), width=4, xs=12, md=4, className="mb-2"),
            dbc.Col(dcc.Graph(id='gust_kph-graph'), width=4, xs=12, md=4, className="mb-2"),
        ], className="mb-3")],
            
            fluid = True)