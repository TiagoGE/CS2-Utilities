from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)

API_VERSION = "0.2.1"

# Load JSON once at startup
with open("videos.json", "r") as f:
    data = json.load(f)

@app.route("/version")
def version():
    return jsonify({"version": API_VERSION})

@app.route("/utilities/<map>/<side>/<site>/<util>", methods=["GET"])
def get_videos(map, side, site, util):

    try:
        videos = data[map][side][site][util]
        return jsonify({"videos": videos})
    except KeyError:
        return jsonify({}), 404
    
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)