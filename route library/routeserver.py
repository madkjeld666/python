from flask import Flask, request, jsonify

app = Flask(__name__)

# Hier word de laatste geupdate route bewaard
laatste_route = {}

@app.route("/upload", methods=["POST"])
def upload_route():
    global laatste_route
    laatste_route = request.get_json()
    return jsonify({"status": "Route ontvangen!"}), 200

@app.route("/view", methods=["GET"])
def view_route():
    if laatste_route:
        return jsonify(laatste_route)
    else:
        return jsonify({"message": "Nog geen route geüpload"}), 404

if __name__ == "__main__":
    app.run(debug=True)
