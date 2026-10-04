from datetime import datetime
import requests


user_input = input("Enter a City name(e.g., London): ")
response = requests.get(f"https://geocoding-api.open-meteo.com/v1/search?name={user_input}")
data = response.json()
city_name = data['results'][0]['name']
print(city_name)
response2 = requests.get("https://api.open-meteo.com/v1/forecast?latitude=LAT&longitude=LON&current_weather=true")

class Weather:
    def __init__(self, city, temperature, windspeed):
        self.city = city
        self.temperature = temperature
        self.windspeed = windspeed

    def summary(self):
        return f"City: {self.city}\nTemperature: {self.temperature}"