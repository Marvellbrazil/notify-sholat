import requests
import locale
from datetime import datetime
import helper
import time
import pytz

# IP API
response = requests.get("http://ip-api.com/json/")
data = response.json()

# General Variables
__CITY__ = data["city"]
__COUNTRY__ = data["country"]
__LANGUAGE__, __ENCODE__ = locale.getlocale()
__ZONEINFO__ = pytz.timezone(data["timezone"])
__NOW__ = datetime.now(__ZONEINFO__)

# Aladhan API
url = "http://api.aladhan.com/v1/timingsByCity"
params = {
    "city": __CITY__,
    "country": __COUNTRY__,
    "method": 20 if __COUNTRY__ == "Indonesia" else 2
}

res = requests.get(url, params = params)
data = res.json()
timings = data["data"]["timings"]

# Time Parsing from API
adzan = ["Fajr", "Dhuhr", "Asr", "Maghrib", "Isha"]
adzan_time = {}
for x in adzan:
    adzan_time[x] = datetime.strptime(timings[x], "%H:%M").replace(
        year = __NOW__.year, month = __NOW__.month, day = __NOW__.day, tzinfo = __ZONEINFO__
    )

# Check
notified = set()
now = __NOW__.strftime("%H:%M")
notified = set()

while True:
    for x in adzan:
        adzan_str = adzan_time[x].strftime("%H:%M")
        if now == adzan_str and x not in notified:
            helper.notify(__LANGUAGE__, x, __CITY__)
            notified.add(x)
    time.sleep(20)