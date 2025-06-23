# webserver.py

from flask import Flask, jsonify
from classes import Lokaal
import json

app = Flask(__name__)

# Route: startpagina
@app.route("/")
def home():
    return "Welkom bij de lokalen route server!"

# Route: geef lokalen als JSON
@app.route("/lokalen")
def get_lokalen():
    lokalen = [
        Lokaal("C1.13", "west"),
        Lokaal("C1.04", "west"),
        Lokaal("C1.06", "west")
    ]
    data = [lokaal.to_dict() for lokaal in lokalen]

    # Sla op in een JSON-bestand (zonder loop)
    with open("lokalen.json", "w") as f:
        json.dump(data, f, indent=4)

    return jsonify(data)

# Server starten
if __name__ == "__main__":
    app.run(debug=True)
