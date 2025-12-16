import os
from winotify import Notification
from playsound import playsound

# PATH
__BASE_DIR__ = os.path.dirname(os.path.abspath(__file__))
__ICON_PATH__ = os.path.join(__BASE_DIR__, "images", "adzan.png")
__SOUND_PATH__ = os.path.join(__BASE_DIR__, "sounds", "adzan-notify-sholat.mp3")

# Main Function
def notify(lang: str, adzan: str, city: str):
    if lang == "Indonesian":
        toast = Notification(
            app_id = "Notify Sholat",
            title = f"Waktunya adzan {adzan}",
            msg = f"Untuk wilayah {city} dan sekitarnya",
            icon = __ICON_PATH__,
        )
    else:
        toast = Notification(
            app_id = "Notify Sholat",
            title = f"It's time for {adzan} prayer",
            msg = f"For {city} and It's nearby",
            icon = __ICON_PATH__,
        )
    
    toast.show()
    playsound(__SOUND_PATH__)