import os
from dotenv import load_dotenv
import requests

load_dotenv()

base_currency = os.getenv("BASE_CURRENCY")
response = requests.get("https://api.frankfurter.app/latest?from=USD")
data = response.json()
user = input("What is your target currency?(e.g, USD) ")
amount = input("How much do you want to convert? ")
for user, rate in data['rates'].items():
    print(f"Currency: {user} | {int(amount) * rate}")