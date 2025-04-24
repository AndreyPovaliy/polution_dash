from dash import Input, Output, html
from utils.data_loader import load_data
import plotly.graph_objects as go

def register_callbacks(app):
   city = 'Москва'
   @app.callback(
        Output('weather-output', 'children'),
        Output('wind_kph-graph', 'figure'),
        Output('pressure_mb-graph', 'figure'),
        Output('humidity-graph', 'figure'),
        Output('cloud-graph', 'figure'),
        Output('uv-graph', 'figure'),
        Output('gust_kph-graph', 'figure'),
        Input('city-input', 'value')
    )

   def update_dashboard(city):
        data = load_data(city)
    
        weather_info = html.Div([
            html.H1(f"{data['city_name']}", className="card-title"),
            html.H3(f"Состояние на {data['current_time']}" , className="card-subtitle"),
            html.P("Скорость ветра (к/ч): " + str(data['current_wind_kph']), className="card-text"),
            html.P("Давление (миллибары): " + str(data['current_pressure_mb']), className="card-text"),
            html.P("Влажность (%): " + str(data['current_humidity']), className="card-text"),
            html.P("Облачный покров (%): " + str(data['current_cloud']), className="card-text"),
            html.P("УФ-индекс: " + str(data['current_uv']), className="card-text"),
            html.P("Порыв ветра (к/ч): " + str(data['current_gust_kph']), className="card-text")
        ])

        wind_kph_fig = go.Figure(
           data=[go.Scatter(x=data['hours'], y=data['wind_kph'], mode='lines+markers', name='wind_kph')],
           layout=go.Layout(title='Скорость ветра:', xaxis_title='Время', yaxis_title='(к/ч)', template='ggplot2') 
        )
        pressure_mb_fig = go.Figure(
           data=[go.Scatter(x=data['hours'], y=data['pressure_mb'], mode='lines+markers', name='pressure_mb')],
           layout=go.Layout(title='Давление', xaxis_title='Время', yaxis_title='(миллибары)', template='ggplot2') 
        )

        humidity_fig = go.Figure(
           data=[go.Scatter(x=data['hours'], y=data['humidity'], mode='lines+markers', name='humidity')],
           layout=go.Layout(title='Влажность', xaxis_title='Время', yaxis_title='(%)', template='ggplot2') 
        )

        cloud_fig = go.Figure(
           data=[go.Scatter(x=data['hours'], y=data['cloud'], mode='lines+markers', name='cloud')],
           layout=go.Layout(title='Облачный покров ', xaxis_title='Время', yaxis_title='(%)', template='ggplot2') 
        )

        uv_fig = go.Figure(
           data=[go.Scatter(x=data['hours'], y=data['uv'], mode='lines+markers', name='uv')],
           layout=go.Layout(title='УФ-индекс', xaxis_title='Время', yaxis_title='(индекс)', template='ggplot2') 
        )

        gust_kph_fig = go.Figure(
           data=[go.Scatter(x=data['hours'], y=data['gust_kph'], mode='lines+markers', name='gust_kph')],
           layout=go.Layout(title='Порыв ветра', xaxis_title='Время', yaxis_title='(к/ч)', template='ggplot2') 
        )
       

          

        return weather_info, wind_kph_fig, pressure_mb_fig, humidity_fig, cloud_fig, uv_fig, gust_kph_fig