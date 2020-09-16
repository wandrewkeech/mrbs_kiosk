#!/usr/bin/python3

import subprocess
import datetime
import time
import json
import os

# Export environment vars for all subprocesses
os.environ['DISPLAY']=":0"
os.environ['XAUTHORITY']="/home/sign/.Xauthority"

# Keep screen from blanking
subprocess.run(["xset", "-dpms", "s", "off", "s", "noblank", "s", "0", "0", "s", "noexpose"])

# Remove cursor from screen
# subprocess.Popen(["unclutter"])

# Set URL variables
base_url = "https://ahvaworkshopbookings.arts.ubc.ca"
today = datetime.date.today()
day = today.strftime("%d")
month = today.strftime("%m")
year = today.strftime("%Y")
pref_path = "/home/sign/.config/chromium/Default/Preferences"
urls = []

# URL Format function
def urlfmt(url, date, area, room):
    return url + "/" + date + ".php?" + "year=" + str(year) + "&month=" + str(month) + "&day=" + str(day) + "&area=" + str(area) + "&room=" + str(room)

# Generate URLs with correct date in slug, pass URL, Area, Rooms
urls.append(urlfmt(base_url, "day", 1, 1))
for i in range(1,6):
    urls.append(urlfmt(base_url, "week", 1, i))

# Override Chromium error/restore bubble
prefs = json.load(open(pref_path, 'r'))
prefs['profile']['exited_cleanly']=True
prefs['profile']['exit_type']="Normal"
with open(pref_path, 'w') as f:
    json.dump(prefs,f)

time.sleep(15)

subprocess.run(["chromium-browser", "--kiosk", "--incognito", "--start-maximized", urls[5], urls[1], urls[2], urls[3], urls[4], urls[0] ])

# Moved tab switching to external process for more reliable display attachment
