from flask import Flask, jsonify, request

app = Flask(__name__)

ALLOWED_ORIGINS = ["http://localhost:3003", "http://localhost:4004"]

@app.route("/", methods=["GET"])
def home():
    return "CORS with Preflight Handling"

@app.route("/api/get-data", methods=["GET", "OPTIONS"])
def get_data():
    origin = request.headers.get("Origin")
    
    if origin not in ALLOWED_ORIGINS:
        return jsonify({"error": "Forbidden"}), 403

    if request.method == "OPTIONS":
        response = app.make_response("")
        response.headers["Access-Control-Allow-Origin"] = origin
        response.headers["Access-Control-Allow-Methods"] = "GET, OPTIONS"
        response.headers["Access-Control-Allow-Headers"] = "Content-Type"
        return response

    response = jsonify({"message": "CORS with Preflight Handling!"})
    response.headers["Access-Control-Allow-Origin"] = origin
    return response

if __name__ == "__main__":
    app.run(port=8080)
