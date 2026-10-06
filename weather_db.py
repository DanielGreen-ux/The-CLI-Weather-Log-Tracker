import sqlite3
from datetime import datetime
import requests

# 1. Database Connection & Table Setup
connection = sqlite3.connect("weather_logs.db")
cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS weather_logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        city TEXT,
        temperature REAL,
        windspeed REAL,
        timestamp TEXT
    )
""")

# 2. User Input & API Request
user_input = input("Enter a City name (e.g., London): ")
response = requests.get(f"https://geocoding-api.open-meteo.com/v1/search?name={user_input}")
data = response.json()

if "results" in data and len(data["results"]) > 0:
    city_name = data["results"][0]["name"]
    longitude = data["results"][0]["longitude"]
    latitude = data["results"][0]["latitude"]

    response2 = requests.get(
        f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"
    )
    data2 = response2.json()

    temperature = data2["current_weather"]["temperature"]
    windspeed = data2["current_weather"]["windspeed"]
    date = datetime.now().strftime("%Y-%m-%d")

    # 3. Insert Record into 'weather_logs'
    cursor.execute(
        "INSERT INTO weather_logs (city, temperature, windspeed, timestamp) VALUES (?, ?, ?, ?)",
        (city_name, temperature, windspeed, date)
    )
    connection.commit()  # Save changes to database

    # 4. Fetch & Display History
    cursor.execute("SELECT * FROM weather_logs")
    stored_records = cursor.fetchall()

    print("\n--- Weather History Logs ---")
    for log in stored_records:
        log_id, city, temp, wind, ts = log
        print(f"ID: {log_id} | City: {city} | Temp: {temp}°C | Wind: {wind} km/h | Date: {ts}")

else:
    print(f"Error: City '{user_input}' not found.")

# 5. Close Connection
connection.close()