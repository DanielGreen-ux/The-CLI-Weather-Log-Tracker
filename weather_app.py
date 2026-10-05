from datetime import datetime
import requests

timestamp = datetime.now().strftime("%Y-%m-%d")

user_input = input("Enter a City name(e.g., London): ")
response = requests.get(f"https://geocoding-api.open-meteo.com/v1/search?name={user_input}")
data = response.json()
city_name = data['results'][0]['name']
longitude = data['results'][0]['longitude']
latitude = data['results'][0]['latitude']

response2 = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true")
data2 = response2.json()
temperature = data2['current_weather']['temperature']
windspeed = data2['current_weather']['windspeed']
class Weather:
    def __init__(self, city, temperature, windspeed):
        self.city = city
        self.temperature = temperature
        self.windspeed = windspeed

    def summary(self):
        return f"City: {self.city} | Temp: {self.temperature}°C | Wind Speed: {self.windspeed} km/h"

user = Weather(city_name, temperature, windspeed)
user_details = user.summary()
print(user_details)
with open("weather_history.txt", "a") as file:
    file.write(f"[{timestamp}] {user_details}\n")