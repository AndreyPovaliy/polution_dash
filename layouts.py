import dash_bootstrap_components as dbc
from dash import dcc

def create_layout():
    return dbc.Container([
        dbc.NavbarSimple(
            brand="Состояние чего-то другого",
            brand_href="#",
            color="primary",
            dark=True,
            className="mb-4 flex justify-content-between"
        ),
        dbc.Row([
            dbc.Col(dbc.Card(id='weather-output', body=True), width=6, xs=12, md=6), 
            dbc.Col([dbc.Input(id = "city-input", type = "text", placeholder = "Введите город", value='Москва')], width = 6, xs = 12, md = 6),
            ], className="mb-3"), 
 
        dbc.Row([
            dbc.Col(dcc.Graph(id='co-graph'), width=4, xs=12, md=4),
            dbc.Col(dcc.Graph(id='no2-graph'), width=4, xs=12, md=4),
            dbc.Col(dcc.Graph(id='o3-graph'), width=4, xs=12, md=4),
        ], className="mb-3"),
  
        dbc.Row([
            dbc.Col(dcc.Graph(id='so2-graph'), width=4, xs=12, md=4),
            dbc.Col(dcc.Graph(id='pm25-graph'), width=4, xs=12, md=4),
            dbc.Col(dcc.Graph(id='pm10-graph'), width=4, xs=12, md=4),
        ], className="mb-3")],
            
            fluid = True)