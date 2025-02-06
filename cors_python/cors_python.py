from flask import Flask, jsonify, request

app = Flask(__name__)

@app.after_request
def apply_cors(response):
    if request.method == "GET":
        response.headers["Access-Control-Allow-Origin"] = "http://localhost:3000"
        response.headers["Access-Control-Allow-Methods"] = "GET"
    return response

@app.route("/")
def home():
    return "Welcome to the CORS-enabled Flask server!"

@app.route("/api/get-data", methods=["GET"])
def get_data():
    return jsonify({"message": "CORS is enabled for GET requests only!"})

if __name__ == "__main__":
    app.run(port=5000)
