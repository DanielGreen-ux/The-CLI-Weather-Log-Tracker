import sqlite3
import requests
from datetime import datetime

connection = sqlite3.connect('weather_logs.db')


cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS logs(id INTEGER PRIMARY KEY AUTOINCREMENT, city TEXT, temperature REAL, windspeed REAL, timestamp TEXT)")
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

date = datetime.now().strftime("%Y-%m-%d")

cursor.execute("INSERT INTO logs(city, temperature, windspeed, timestamp) VALUES (?,?,?,?)" ,(city_name,temperature,windspeed,date))

connection.commit()

connection.execute("SELECT * FROM logs")
stored_records = connection.fetchall()
print(stored_records)