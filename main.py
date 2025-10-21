# CS2 helper Prototype

import requests
import webbrowser
import os

from version import get_latest_version_info

APP_VERSION, RELEASE_DATE = get_latest_version_info()
print(f"Version- [{APP_VERSION}] ({RELEASE_DATE})\n")

def clear_console():
    # Windows
    if os.name == "nt":
        os.system("cls")
    # Mac / Linux
    else:
        os.system("clear")

# The base URL of API (local for now)
BASE_URL = "http://127.0.0.1:5000/utilities"

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
url = f"{BASE_URL}/{map_key}/{side_key}/{site_key}/{util_key}"
print(url)
response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    # Access the nested "videos" dictionary
    videos = data.get("videos", {})  # returns {} if "videos" key doesn't exist
    
    if videos:
        print("==> Available videos:\n")

        # Convert dictionary items into a list for stable indexing
        video_list = list(videos.items())  # [(spot, url), ...]

        # Display numbered list for user
        for i, (spot, _) in enumerate(video_list):
            print(f"{i} - {spot}")
        
        # Get user's choice
        choice = int(input("\nChoose a video (enter number): "))

        # Safely get the URL corresponding to the choice
        selected_url = video_list[choice][1]

        print(f"\nOpening: {selected_url}")
        webbrowser.open(selected_url)
        
    else:
        print("⚠️ Could not get utility info.")
else:
    print(f"Error {response.status_code}: Unable to reach API.")

