from flask import Flask, jsonify
import json
import os, sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from  version import get_latest_version_info

app = Flask(__name__)

APP_VERSION, RELEASE_DATE = get_latest_version_info()
print(f"{APP_VERSION} / {RELEASE_DATE}")

DATA_FILE = "videos.json"

# Load JSON once at startup
if os.path.exists(DATA_FILE):
    with open(DATA_FILE, "r") as f:
        data = json.load(f)
else:
    data = {}


@app.route("/version")
def version():
    return jsonify({
        "version": APP_VERSION,
        "release_date": RELEASE_DATE
    })

@app.route("/utilities/<map>/<side>/<site>/<util>", methods=["GET"])
def get_videos(map, side, site, util):

    try:
        videos = data[map][side][site][util]
        return jsonify({"videos": videos})
    except KeyError:
        return jsonify({}), 404
    
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)