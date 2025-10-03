from flask import Flask, jsonify
from flask_cors import CORS
import random
import time

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Simulate some dynamic data
@app.route("/api/data")
def get_data():
    time.sleep(random.uniform(0.1, 0.5))  # Simulate processing time
    data = {
        "status": "success",
        "value": random.randint(1, 100),
        "message": "Hello from backend!"
    }
    return jsonify(data)

@app.route("/")
def home():
    return "Backend is running!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
