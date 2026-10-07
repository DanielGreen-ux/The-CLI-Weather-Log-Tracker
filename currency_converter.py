import os
from dotenv import load_dotenv
import requests

load_dotenv()

base_currency = os.getenv("BASE_CURRENCY")
response = requests.get(f"https://api.frankfurter.app/latest?from={base_currency}")
data = response.json()
rate = data['rates']
user = input("What is your target currency?(e.g, USD) ").strip().upper()
try:
    amount = input("How much do you want to convert? ")
    amount = int(amount)
except ValueError:
    print("Invalid input. Please enter a valid number.")
    exit()

fetch = rate.get(user)
if not fetch:
    print("Invalid currency. Please enter a valid currency code.")
    exit()
print(f"Currency: ${amount} {base_currency} = {amount * fetch:.2f} {user}")