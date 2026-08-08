import requests
from config import API_KEY, CURRENT_URL


def get_weather(city):

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    response = requests.get(CURRENT_URL, params=params)

    return response.json()