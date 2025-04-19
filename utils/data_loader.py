from dotenv import load_dotenv
import os
import requests

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_URL = os.getenv("API_URL")
DAYS = 1
LANG = 'ru'
AQI = 'yes'


def load_data(city):
    response = requests.get(API_URL, params={'key': API_KEY, 'q': city, 'days': DAYS, 'aqi': AQI, 'lang': LANG})
    data = response.json()
    location = data['location']
    forecast_hours = data['forecast']['forecastday'][0]['hour']
    city_name = location['name']
    current_time = location['localtime']
    current_air = data['current']['air_quality']
    current_co = current_air['co']
    current_no2 = current_air['no2']
    current_o3 = current_air['o3']
    current_so2 = current_air['so2']
    current_pm2_5 = current_air['pm2_5']
    current_pm10 = current_air['pm10']
    hours = [h['time'][-5:] for h in forecast_hours]
    co = [h['air_quality']['co'] for h in forecast_hours]
    no2 = [h['air_quality']['no2'] for h in forecast_hours]
    o3 = [h['air_quality']['o3'] for h in forecast_hours]
    so2 = [h['air_quality']['so2'] for h in forecast_hours]
    pm2_5 = [h['air_quality']['pm2_5'] for h in forecast_hours]
    pm10 = [h['air_quality']['pm10'] for h in forecast_hours]
    return {"location": location,
            "city_name": city_name,
            "current_time":current_time,
            "current_co": current_co,
            "current_no2": current_no2,
            "current_o3": current_o3,
            "current_so2": current_so2,
            "current_pm2_5": current_pm2_5,
            "current_pm10": current_pm10,
            "hours": hours,
            "co": co,
            "no2":no2,
            "o3":o3,
            "so2":so2,
            "pm2_5":pm2_5,
            "pm10":pm10}
