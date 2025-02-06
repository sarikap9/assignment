from flask import Flask, jsonify, request

app = Flask(__name__)

ALLOWED_ORIGINS = ["http://localhost:3000", "http://localhost:4000"]

@app.after_request
def apply_cors(response):
    origin = request.headers.get("Origin")
    if origin in ALLOWED_ORIGINS and request.method == "GET":
        response.headers["Access-Control-Allow-Origin"] = origin
        response.headers["Access-Control-Allow-Methods"] = "GET"
        response.headers["Access-Control-Allow-Headers"] = "Content-Type"
    return response

@app.route("/", methods=["GET"])
def home():
    return "Multiple Origins CORS Server"

@app.route("/api/get-data", methods=["GET"])
def get_data():
    return jsonify({"message": "CORS enabled for multiple origins!"})

if __name__ == "__main__":
    app.run(port=5001)
