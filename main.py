# CS2 helper Prototype

import requests
import webbrowser
import os


def clear_console():
    # Windows
    if os.name == "nt":
        os.system("cls")
    # Mac / Linux
    else:
        os.system("clear")

# The base URL of your API (local for now)
BASE_URL = "http://127.0.0.1:5000/videos"

maps = ["Mirage", "Dust", "Inferno"]
sides = ["Terrorist", "Counter-Terrorist"]
sites = ["Bomb A", "Bomb B", "Mid"]
utilities = ["Granane", "Flash", "Smoke", "Molotov"]

# --> ask for inputs <--
print("Choose a map:")
for i, m in enumerate(maps):
    print(f"{i} - {m}")
map_choice = int(input("Input: "))
clear_console()

print("Choose a side:")
for i, s in enumerate(sides):
    print(f"{i} - {s}")
side_choice = int(input("Input: "))
clear_console()

print("Choose bomb site:")
for i, site in enumerate(sites):
    print(f"{i} - {site}")
site_choice = int(input("Input: "))
clear_console()

print("Choose a utility:")
for i, u in enumerate(utilities):
    print(f"{i} - {u}")
util_choice = int(input("Input: "))
clear_console()


# Build keys to access JSON
# -------------------------
map_key = maps[map_choice]
side_key = "T" if side_choice == 0 else "CT"
site_key = "A" if site_choice == 0 else "B" if site_choice == 1 else "Mid"
util_key = utilities[util_choice]

# Build the API URL
url = f"{BASE_URL}/utilities/{map_key}/{side_key}/{site_key}/{util_key}"
print(url)
response = requests.get(url)

if response.status_code == 200:
    videos = response.json()
    
    if videos:
        print("==> Available videos:")
        for i, (spot, video_url) in enumerate(videos.items()):
            print(f"{i} - {spot} -> {video_url}")

        choice = int(input("Choose a video: "))
        selected_url = list(videos.values())[choice]

        print(f"Opening: {selected_url}")
        webbrowser.open(video_url)
    else:
        print("⚠️ Could not get utility info.")
else:
    print(f"Error {response.status_code}: Unable to reach API.")

