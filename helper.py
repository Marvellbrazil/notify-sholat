import os
from winotify import Notification
from playsound import playsound

# PATH
__BASE_DIR__ = os.path.dirname(os.path.abspath(__file__))
__ICON_PATH__ = os.path.join(__BASE_DIR__, "images", "adzan.png")
__SOUND_PATH__ = os.path.join(__BASE_DIR__, "sounds", "adzan-notify-sholat.mp3")

# Main Function
def notify(lang, adzan: str, city: str):
    translations = {
        "Fajr": "Subuh",
        "Dhuhr": "Dzuhur",
        "Asr": "Ashar",
        "Maghrib": "Maghrib",
        "Isha": "Isya"
    }

    if lang.startswith("id"):
        title = f"Waktunya adzan {translations[adzan]}"
        msg = f"Untuk wilayah {city} dan sekitarnya"
    else:
        title = f"It's time for {adzan} prayer"
        msg = f"For {city} and nearby"
    
    toast = Notification(
        app_id="Notify Sholat",
        title=title,
        msg=msg,
        icon=__ICON_PATH__,
    )
    
    toast.show()
    playsound(__SOUND_PATH__)