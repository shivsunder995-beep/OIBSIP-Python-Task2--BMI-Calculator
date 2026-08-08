import requests
from config import API_KEY, FORECAST_URL


def get_forecast(city):

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    response = requests.get(FORECAST_URL, params=params)

    return response.json()