# ==========================
# Imports
# ==========================
import tkinter as tk

from weather import get_weather
from forecast import get_forecast
from location import get_current_city
from theme import blue_theme
from search import search_city
from utils import format_time, current_date, current_time

# ==========================
# Get Current Weather
# ==========================
city = get_current_city()
weather = get_weather(city)
forecast = get_forecast(city)

# ==========================
# Window
# ==========================
root = tk.Tk()
root.title("Python Weather Dashboard")
root.geometry("750x900")
root.resizable(True, True)

blue_theme(root)

# ==========================
# Fonts
# ==========================
TITLE_FONT = ("Arial", 24, "bold")
HEADING_FONT = ("Arial", 18, "bold")
TEXT_FONT = ("Arial", 16)
CLOCK_FONT = ("Arial", 24, "bold")
FORECAST_FONT = ("Arial", 14)

# ==========================
# Search Box
# ==========================
cityEntry = tk.Entry(
    root,
    font=("Arial", 16),
    width=25,
    justify="center"
)
cityEntry.insert(0, city)
cityEntry.pack(pady=15)

# ==========================
# Heading
# ==========================
title = tk.Label(
    root,
    text="🌤 Python Weather Dashboard",
    font=TITLE_FONT
)
title.pack(pady=10)

# ==========================
# Weather Information Frame
# ==========================
weatherFrame = tk.Frame(root)
weatherFrame.pack(pady=10)

cityLabel = tk.Label(weatherFrame, font=HEADING_FONT)
cityLabel.pack(pady=6)

temp = tk.Label(weatherFrame, font=TEXT_FONT)
temp.pack(pady=4)

condition = tk.Label(weatherFrame, font=TEXT_FONT)
condition.pack(pady=4)

humidity = tk.Label(weatherFrame, font=TEXT_FONT)
humidity.pack(pady=4)

wind = tk.Label(weatherFrame, font=TEXT_FONT)
wind.pack(pady=4)

pressure = tk.Label(weatherFrame, font=TEXT_FONT)
pressure.pack(pady=4)

sunrise = tk.Label(weatherFrame, font=TEXT_FONT)
sunrise.pack(pady=4)

sunset = tk.Label(weatherFrame, font=TEXT_FONT)
sunset.pack(pady=4)

dateLabel = tk.Label(
    weatherFrame,
    text=current_date(),
    font=("Arial", 15)
)
dateLabel.pack(pady=8)

clock = tk.Label(
    weatherFrame,
    font=CLOCK_FONT
)
clock.pack(pady=10)

# ==========================
# Forecast Title
# ==========================
forecastTitle = tk.Label(
    root,
    text="📅 5-Day Forecast",
    font=HEADING_FONT
)
forecastTitle.pack(pady=15)

# ==========================
# Forecast Frame
# ==========================
forecastFrame = tk.Frame(root)
forecastFrame.pack(pady=10)

# ==========================
# Display Weather
# ==========================
def display_weather(weather, forecast):

    cityLabel.config(text=f"📍 City : {weather['name']}")

    temp.config(
        text=f"🌡 Temperature : {weather['main']['temp']} °C"
    )

    condition.config(
        text=f"☁ Condition : {weather['weather'][0]['description'].title()}"
    )

    humidity.config(
        text=f"💧 Humidity : {weather['main']['humidity']} %"
    )

    wind.config(
        text=f"🌬 Wind : {weather['wind']['speed']} m/s"
    )

    pressure.config(
        text=f"📊 Pressure : {weather['main']['pressure']} hPa"
    )

    sunrise.config(
        text=f"🌅 Sunrise : {format_time(weather['sys']['sunrise'])}"
    )

    sunset.config(
        text=f"🌇 Sunset : {format_time(weather['sys']['sunset'])}"
    )

    dateLabel.config(text="📅 " + current_date())

    # Clear old forecast
    for widget in forecastFrame.winfo_children():
        widget.destroy()

    # Display first five forecast entries
    for item in forecast["list"][:5]:

        forecastText = (
            f"{item['dt_txt']}    |    "
            f"{item['main']['temp']}°C    |    "
            f"{item['weather'][0]['main']}"
        )

        tk.Label(
            forecastFrame,
            text=forecastText,
            font=FORECAST_FONT,
            anchor="w"
        ).pack(anchor="w", pady=6)

# Show Weather
display_weather(weather, forecast)

# ==========================
# Search Function
# ==========================
def search():

    city = cityEntry.get().strip()

    if city == "":
        return

    try:
        weather, forecast = search_city(city)
        display_weather(weather, forecast)

    except Exception:
        cityLabel.config(text="❌ City not found!")

# ==========================
# Search Button
# ==========================
searchButton = tk.Button(
    root,
    text="🔍 Search",
    font=("Arial", 15, "bold"),
    padx=20,
    pady=8,
    command=search
)
searchButton.pack(pady=5)

# ==========================
# Clock
# ==========================
def update_clock():
    clock.config(text="🕒 " + current_time())
    root.after(1000, update_clock)

update_clock()

# ==========================
# Run App
# ==========================
root.mainloop()