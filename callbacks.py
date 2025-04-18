from dash import Input, Output, html
from utils.data_loader import load_data
import plotly.graph_objects as go

def register_callbacks(app):
    @app.callback(
        Output('weather-output', 'children'),
        Output('co-graph', 'figure'),
        Output('no2-graph', 'figure'),
        Output('o3-graph', 'figure'),
        Output('so2-graph', 'figure'),
        Output('pm25-graph', 'figure'),
        Output('pm10-graph', 'figure'),
        Input('city-input', 'value')
    )
    def update_dashboard(city):
        data = load_data(city)
    
        weather_info = html.Div([
            html.H4(f"{data['city_name']}", className="card-title"),
            html.Img(src=f"https:{data['icon']}", style={"height": "64px"}),
            html.H5(f"{data['temp']}°C", className="card-subtitle mb-2 text-muted"),
            html.P(data['condition'], className="card-text")
        ])

        co_fig = go.Figure(
           data=[go.Scatter(x=data['hours'], y=data['co'], mode='lines+markers', name='CO')],
           layout=go.Layout(title='График No1 CO', xaxis_title='Время', yaxis_title='CO', template='gridon') 
        )
        no2_fig = go.Figure(
           data=[go.Scatter(x=data['hours'], y=data['no2'], mode='lines+markers', name='NO2')],
           layout=go.Layout(title='График No2 NO2', xaxis_title='Время', yaxis_title='NO2', template='gridon') 
        )

        o3_fig = go.Figure(
           data=[go.Scatter(x=data['hours'], y=data['o3'], mode='lines+markers', name='O3')],
           layout=go.Layout(title='График No3 O3', xaxis_title='Время', yaxis_title='NO2', template='gridon') 
        )

        so2_fig = go.Figure(
           data=[go.Scatter(x=data['hours'], y=data['so2'], mode='lines+markers', name='SO2')],
           layout=go.Layout(title='График No4 SO2', xaxis_title='Время', yaxis_title='SO2', template='gridon') 
        )

        pm2_5_fig = go.Figure(
           data=[go.Scatter(x=data['hours'], y=data['pm2_5'], mode='lines+markers', name='PM2_5')],
           layout=go.Layout(title='График No5 PM2_5', xaxis_title='Время', yaxis_title='PM2_5', template='gridon') 
        )

        pm10_fig = go.Figure(
           data=[go.Scatter(x=data['hours'], y=data['pm10'], mode='lines+markers', name='PM10')],
           layout=go.Layout(title='График No6 PM10', xaxis_title='Время', yaxis_title='PM10', template='gridon') 
        )
       

          

        return weather_info, co_fig, no2_fig, o3_fig, so2_fig, pm2_5_fig, pm10_fig