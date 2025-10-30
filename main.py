import requests
import webbrowser
import os
import time
from version import get_latest_version_info
from spinner import DotSpinner

APP_VERSION, RELEASE_DATE = get_latest_version_info()
API_URL = "https://cs2-quickutil.onrender.com"
update_message = ""

def clear_console():
    os.system("cls" if os.name == "nt" else "clear")
    

def warm_up_api():
    print("\nWaking up servers, please wait...")
    spinner = DotSpinner("Zzz ")
    spinner.start()

    attempts = 0
    while attempts < 6:
        try:
            response = requests.get(f"{API_URL}/")
            if response.status_code == 200:
                spinner.stop("✅ Servers ready!")
                return
        except:
            pass
        time.sleep(4)
        attempts += 1

    spinner.stop("⚠️ API still waking up")
    time.sleep(1)


def check_update():
    try:
        response = requests.get(f"{API_URL}/version")
        if response.status_code == 200:
            latest_version = response.json().get("version")
            if latest_version != APP_VERSION:
                return(f"🟡 Update available: v{latest_version}")
            else:
                return("✅ You are up to date!")
    except:
        return("⚠️ Could not check for updates.")


def get_valid_input(prompt, valid_options):
    while True:
        choice = input(prompt).strip()

        if choice.isdigit():
            choice = int(choice)
            if choice in valid_options:
                return choice

        print("❌ Invalid input. Please try again.\n")


def main_menu():
    clear_console()
    print(f"┌────────────────────────────────┐")
    print(f"│  CS2 Quick Utilities           │  v{APP_VERSION}")
    print(f"├────────────────────────────────┤")
    print(f"│ 1 • Mirage                     │")
    print(f"│ 2 • Dust2                      │")
    print(f"│ 3 • Inferno                    │")
    print(f"│ 0 • Exit                       │")
    print(f"└────────────────────────────────┘")
    print(update_message)
    return get_valid_input("\nSelect map: ", [0, 1, 2, 3])


def resolve_keys(map_choice, side_choice, site_choice, util_choice):
    map_keys = {1: "Mirage", 2: "Dust2", 3: "Inferno"}
    side_keys = {1: "T", 2: "CT"}
    site_keys = {1: "A", 2: "B", 3: "Mid"}
    util_keys = {1: "Smoke", 2: "flash", 3: "molotov"}

    return (map_keys.get(map_choice),
            side_keys.get(side_choice),
            site_keys.get(site_choice),
            util_keys.get(util_choice))


def fetch_and_open_videos(map_key, side_key, site_key, util_key):
    url = f"{API_URL}/utilities/{map_key}/{side_key}/{site_key}/{util_key}"
    response = requests.get(url)

    if response.status_code != 200:
        print("⚠️ No utilities found for that selection!")
        input("\nPress Enter to return...")
        return

    data = response.json()
    videos = data.get("videos", {})

    if not videos:
        print("⚠️   No videos available yet.")
        input("\nPress Enter to return...")
        return

    # Show video list
    video_list = list(videos.items())
    print("\n==> Available Videos:\n")
    for i, (spot, _) in enumerate(video_list):
        print(f"{i} - {spot}")

    choice = get_valid_input("\nChoose a video: ",
                             list(range(len(video_list))))
    webbrowser.open(video_list[choice][1])
    print("\n✅ Video opened!")


if __name__ == "__main__":
    warm_up_api()

    update_message = update_message = check_update() # check update only once

    while True:
        map_choice = main_menu()

        if map_choice == 0:
            print("\nGoodbye! 👋")
            break
        clear_console()

        side_choice = get_valid_input("Side (1=T | 2=CT | 0=Back): ", [0, 1, 2])
        if side_choice == 0:
            continue
        clear_console()

        site_choice = get_valid_input("Site (1=A | 2=B | 3=Mid | 0=Back): ", [0, 1, 2, 3])
        if site_choice == 0:
            continue
        clear_console()
        
        util_choice = get_valid_input("Utility (1=Smoke | 2=Flash | 3=Molotov | 0=Back): ", [0, 1, 2, 3])
        if util_choice == 0:
            continue
        clear_console()

        keys = resolve_keys(map_choice, side_choice, site_choice, util_choice)
        fetch_and_open_videos(*keys)