from dotenv import load_dotenv
import os
import requests

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_URL = os.getenv("API_URL")
DAYS = 1
LANG = 'ru'
AQI = 'yes'
# city = 'Москва'


def load_data(city):
    response = requests.get(API_URL, params={'key': API_KEY, 'q': city, 'days': DAYS, 'aqi': AQI, 'lang': LANG})
    data = response.json()
    location = data['location']
    forecast_hours = data['forecast']['forecastday'][0]['hour']
    city_name = location['name']
    current_time = location['localtime']
    current = data['current']
    current_wind_kph = current['wind_kph']
    current_pressure_mb = current['pressure_mb']
    current_humidity = current['humidity']
    current_cloud = current['cloud']
    current_uv = current['uv']
    current_gust_kph = current['gust_kph']
    hours = [h['time'][-5:] for h in forecast_hours]
    wind_kph = [h['wind_kph'] for h in forecast_hours]
    pressure_mb = [h['pressure_mb'] for h in forecast_hours]
    humidity = [h['humidity'] for h in forecast_hours]
    cloud = [h['cloud'] for h in forecast_hours]
    uv = [h['uv'] for h in forecast_hours]
    gust_kph = [h['uv'] for h in forecast_hours]
   
    return {"location": location,
            "city_name": city_name,
            "current_time":current_time,
            "current_wind_kph": current_wind_kph,
            "current_pressure_mb": current_pressure_mb,
            "current_humidity": current_humidity,
            "current_cloud": current_cloud,
            "current_uv": current_uv,
            "current_gust_kph": current_gust_kph,
            "hours": hours,
            "wind_kph": wind_kph,
            "pressure_mb":pressure_mb,
            "humidity":humidity,
            "cloud":cloud,
            "uv":uv,
            "gust_kph":gust_kph}
