import requests

API_KEY = "fca_live_yzACKSIG8zO3vKR1j9xpJRmAEZEqBafLqEAf5dBj"
BASE_URL = f"https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}"

CURRENCIES = ['CAD', 'EUR', 'USD', 'CNY']

def convert_currency(base):
    currencies = ','.join(CURRENCIES)
    url = f"{BASE_URL}&base_currency={base}&currencies={currencies}"

    try:
        response = requests.get(url)
        data = response.json()
        print(data)
        return data
    except Exception as e:
        print(e)
        return None

convert_currency("USD")