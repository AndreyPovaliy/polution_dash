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
            html.H6(f"Состояние на {data['current_time']}" , className="card-subtitle"),
            html.P("Углекислый газ: " + str(data['current_co']), className="card-text"),
            html.P("Оксид азота: " + str(data['current_no2']), className="card-text"),
            html.P("Озон: " + str(data['current_o3']), className="card-text"),
            html.P("Оксид серы: " + str(data['current_so2']), className="card-text"),
            html.P("Мельчайшие частицы: " + str(data['current_pm2_5']), className="card-text"),
            html.P("Твердые частицы: " + str(data['current_pm10']), className="card-text")
        ])

        co_fig = go.Figure(
           data=[go.Scatter(x=data['hours'], y=data['co'], mode='lines+markers', name='co')],
           layout=go.Layout(title='График No1 Углекислый газ', xaxis_title='Время', yaxis_title='CO', template='ggplot2') 
        )
        no2_fig = go.Figure(
           data=[go.Scatter(x=data['hours'], y=data['no2'], mode='lines+markers', name='no2')],
           layout=go.Layout(title='График No2 Оксид азота', xaxis_title='Время', yaxis_title='NO2', template='ggplot2') 
        )

        o3_fig = go.Figure(
           data=[go.Scatter(x=data['hours'], y=data['o3'], mode='lines+markers', name='o3')],
           layout=go.Layout(title='График No3 Озон', xaxis_title='Время', yaxis_title='O3', template='ggplot2') 
        )

        so2_fig = go.Figure(
           data=[go.Scatter(x=data['hours'], y=data['so2'], mode='lines+markers', name='so2')],
           layout=go.Layout(title='График No4 Оксид серы', xaxis_title='Время', yaxis_title='SO2', template='ggplot2') 
        )

        pm2_5_fig = go.Figure(
           data=[go.Scatter(x=data['hours'], y=data['pm2_5'], mode='lines+markers', name='pm2_5')],
           layout=go.Layout(title='График No5 Мельчайшие частицы', xaxis_title='Время', yaxis_title='PM2_5', template='ggplot2') 
        )

        pm10_fig = go.Figure(
           data=[go.Scatter(x=data['hours'], y=data['pm10'], mode='lines+markers', name='pm10')],
           layout=go.Layout(title='График No6 Твердые частицы', xaxis_title='Время', yaxis_title='PM10', template='ggplot2') 
        )
       

          

        return weather_info, co_fig, no2_fig, o3_fig, so2_fig, pm2_5_fig, pm10_fig