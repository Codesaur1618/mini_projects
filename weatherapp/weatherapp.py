import tkinter as tk
import requests
import json
import geocoder

# Create the main application window
root = tk.Tk()
root.title("Weather App")

# Create and place widgets within the window

# Create labels
label_location = tk.Label(root, text="Your Location: ")
label_weather = tk.Label(root, text="Weather: ")
label_temperature = tk.Label(root, text="Temperature: ")
label_humidity = tk.Label(root, text="Humidity: ")
label_wind = tk.Label(root, text="Wind Speed: ")

# Create a function to fetch weather data based on the user's location
def fetch_weather():
    try:
        # Detect the user's location based on IP address
        user_location = geocoder.ip('me')
        latitude, longitude = user_location.latlng

        # Replace "YOUR_API_KEY" with your actual OpenWeatherMap API key
        api_key = "YOUR_API_KEY"
        base_url = "https://api.openweathermap.org/data/2.5/weather"
        params = {
            "lat": latitude,
            "lon": longitude,
            "appid": api_key,
            "units": "metric"
        }

        response = requests.get(base_url, params=params)
        if response.status_code == 200:
            weather_data = json.loads(response.text)
            location_name = weather_data["name"]
            weather_description = weather_data["weather"][0]["description"]
            temperature = weather_data["main"]["temp"]
            humidity = weather_data["main"]["humidity"]
            wind_speed = weather_data["wind"]["speed"]

            label_location.config(text=f"Your Location: {location_name}")
            label_weather.config(text=f"Weather: {weather_description}")
            label_temperature.config(text=f"Temperature: {temperature}°C")
            label_humidity.config(text=f"Humidity: {humidity}%")
            label_wind.config(text=f"Wind Speed: {wind_speed} m/s")
        else:
            label_location.config(text="Location data not available.")
            label_weather.config(text="Weather data not available.")
            label_temperature.config(text="")
            label_humidity.config(text="")
            label_wind.config(text="")

    except Exception as e:
        label_location.config(text="Error detecting location.")
        label_weather.config(text="")
        label_temperature.config(text="")
        label_humidity.config(text="")
        label_wind.config(text="")

# Create a button to trigger weather data retrieval
button_fetch = tk.Button(root, text="Get Weather", command=fetch_weather)

# Place widgets in the window
label_location.pack()
label_weather.pack()
label_temperature.pack()
label_humidity.pack()
label_wind.pack()
button_fetch.pack()

# Start the main GUI loop
root.mainloop()
