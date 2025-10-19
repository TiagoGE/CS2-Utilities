# CS2 Utilities

**CS2 Utilities** is a helper tool for CS2 players to quickly find and watch short videos of utilities (smokes, flashes, molotovs, grenades) for specific maps, sides, bomb sites, and spots.

---

## Features

- Console-based interface for selecting map, side, site, and utility
- Retrieves video links via a Flask API
- Opens selected videos in the default web browser
- Designed for quick reference before or during gameplay
- Works locally or via API for easy sharing with friends

---

## Installation

```bash
1. Clone the repository:
git clone https://github.com/yourusername/CS2-Utilities.git

2. Navigate into the project folder:
cd CS2-Utilities

3. Install dependencies for the API:
cd api
pip install -r requirements.txt

4. Run the API locally:
python app.py

5. Open a new terminal and run the client interface:
python app.py


#Usage
Choose a map (Mirage, Dust, Inferno)
Choose a side (T or CT)
Choose a bomb site (A, B, Mid)
Choose a utility (Grenade, Flash, Smoke, Molotov)
Select the spot from the available videos
The video opens in your default browser

#Changelog
For a detailed history of updates, see CHANGELOG.md

#Credits
Created by Tiago Guerra Endsfeldz

#License
This project is licensed under the MIT License - see the LICENSE
 file for details.
You are free to use, copy, and run the executable. You may also modify the code if you wish, as long as the original copyright notice is included.