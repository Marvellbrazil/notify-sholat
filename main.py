import requests
import locale

# IP API
response = requests.get("http://ip-api.com/json/")
data = response.json()

# General Variables
__CITY__ = data["city"]
__COUNTRY__ = data["country"]
__LANGUAGE__ = locale.getlocale()

# Aladhan API
url = "http://api.aladhan.com/v1/timingsByCity"
params = {
    "city": __CITY__,
    "country": __COUNTRY__,
    "method": 2
}
res = requests.get(url, params = params)
data = res.json()