from weather import get_weather
from forecast import get_forecast


def search_city(city):

    weather = get_weather(city)

    forecast = get_forecast(city)

    return weather, forecast