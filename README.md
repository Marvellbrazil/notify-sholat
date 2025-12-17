
<h1 align="center">notify-sholat</h1>

<p align="center">
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge"/></a>
  <a href="https://docs.python-requests.org/"><img src="https://img.shields.io/badge/Requests-HTTP-lightgrey?style=for-the-badge"/></a>
  <a href="https://docs.python.org/3/library/locale.html"><img src="https://img.shields.io/badge/Locale-i18n-yellow?style=for-the-badge"/></a>
  <a href="https://docs.python.org/3/library/datetime.html"><img src="https://img.shields.io/badge/Datetime-Time%20Handling-purple?style=for-the-badge"/></a>
  <a href="https://docs.python.org/3/library/time.html"><img src="https://img.shields.io/badge/Time-Scheduler-blueviolet?style=for-the-badge"/></a>
  <a href="https://pypi.org/project/pytz/"><img src="https://img.shields.io/badge/Pytz-Timezone-green?style=for-the-badge"/></a>
  <a href="https://docs.python.org/3/library/os.html"><img src="https://img.shields.io/badge/OS-System-orange?style=for-the-badge"/></a>
  <a href="https://pypi.org/project/winotify/"><img src="https://img.shields.io/badge/Winotify-Windows%20Notification-lightblue?style=for-the-badge"/></a>
  <a href="https://pypi.org/project/playsound/"><img src="https://img.shields.io/badge/Playsound-Audio-red?style=for-the-badge"/></a>
  <a href="http://api.aladhan.com/v1/timingsByCity"><img src="https://img.shields.io/badge/Aladhan-API-brightgreen?style=for-the-badge"/></a>
  <a href="https://ipapi.co/"><img src="https://img.shields.io/badge/IP%20API-GeoLocation-9cf?style=for-the-badge"/></a>
  <a href="https://github.com/Marvellbrazil/mypygui/blob/main/LICENSE"><img src="https://img.shields.io/github/license/Marvellbrazil/mypygui?style=for-the-badge"/></a>
</p>

A simple Python project created to help Muslims stay mindful of their five daily prayers while working on a laptop. It runs quietly in the background, checking prayer times based on your location and sending a gentle reminder so you don’t lose track of time during busy activities. The idea is straightforward, to keep focus on your work, but never forget the call to prayer.

---

## Table of Contents

- [Overview](#overview)
- [Technologies](#technologies)
- [Prerequisites](#prerequisites)
- [Installation & Setup](#installation--setup)
- [Usage](#usage)
- [Folder Structure](#folder-structure)
- [How It Works](#how-it-works)
- [Contributing](#contributing)
- [License](#license)

---

## Overview

**notify-sholat** is a reminder for muslims out there because, sometimes we get so absorbed in our activities that we lose track of time and end up praying at the last minute. This tool helps raise awareness by sending timely reminders, so we don’t forget the call to prayer amidst our busy schedules.

With this lightweight program, I hope it can serve as a gentle nudge to pause, reflect, and fulfill our daily prayers on time.

---

## Technologies

- **Python 3.11**
- **Requests**
- **Locale**
- **Datetime**
- **Time**
- **Pytz**
- **OS**
- **Winotify**
- **Playsound**

---

## Prerequisites

Make sure you have:

- Python 3.x installed
- Required Python package :

<code>Bash</code>
```bash
git clone https://github.com/Marvellbrazil/notify-sholat.git
cd notify-sholat

python -m venv venv
venv\Scripts\activate

pip install requests pytz winotify playsound
```

---

## Run

To run, type this in the terminal :

<code>Bash</code>
```bash
python main.py
```
