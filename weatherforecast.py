import requests
import tkinter as tk
from tkinter import messagebox
import os

api_key = os.environ ['weather_api_key']
api_url = "http://api.openweathermap.org/data/2.5/weather"

BACKGROUND_COLOR = "snow"
FONT_STYLE = ("Helvetica", 12)
LABEL_WIDTH = 20
BUTTON_WIDTH = 15
TEXTBOX_WIDTH = 30

class WeatherApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Weather Forecast App")
        self.geometry("400x400")
        self.configure(bg=BACKGROUND_COLOR)

        self.label = tk.Label(self, text="Enter city or zip code", font=FONT_STYLE, bg=BACKGROUND_COLOR)
        self.label.pack(pady=10)

        self.city_entry = tk.Entry(self, font=FONT_STYLE, width=TEXTBOX_WIDTH)
        self.city_entry.pack(pady=10)

        self.get_weather_button = tk.Button(self, text="Show Weather",bg="wheat2" ,font=FONT_STYLE, width=BUTTON_WIDTH, command=self.get_weather)
        self.get_weather_button.pack(pady=10)

        self.weather_info_label = tk.Label(self, text="", font=FONT_STYLE, bg=BACKGROUND_COLOR, justify="left")
        self.weather_info_label.pack(pady=10)

    def get_weather(self):
        user_input = self.city_entry.get()
        weather_data = self.fetch_weather_data(user_input)

        if weather_data:
            self.display_weather(weather_data)
        else:
            messagebox.showerror("Error", "City not found or API request failed.")

    def fetch_weather_data(self, user_input):
        params = {
            "q": user_input,
            "appid": api_key,
            "units": "metric"
        }

        response = requests.get(api_url, params=params)
        data = response.json()

        if data["cod"] == 200:
            weather_data = {
                "temperature": data["main"]["temp"],
                "humidity": data["main"]["humidity"],
                "wind_speed": data["wind"]["speed"],
                "description": data["weather"][0]["description"]
            }
            return weather_data
        else:
            return None

    def display_weather(self, weather_data):
        result_text=f"Temperature: {weather_data['temperature']}°C\n" \
                    f"Humidity: {weather_data['humidity']}%\n" \
                    f"Wind Speed: {weather_data['wind_speed']} m/s\n" \
                    f"Description: {weather_data['description']}"

        self.weather_info_label.config(text=result_text)

if __name__ == "__main__":
    app = WeatherApp()
    app.mainloop()
