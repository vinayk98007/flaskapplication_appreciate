from flask import Flask, jsonify
import logging
import sys

app = Flask(__name__)

# Configure logging to file and stdout
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s: %(message)s",
    handlers=[
        logging.FileHandler("/var/log/app.log"),  # file for Promtail
        logging.StreamHandler(sys.stdout)         # stdout for ECS debugging
    ]
)

@app.route("/")
def home():
    app.logger.info("Home endpoint called")
    return jsonify(message="Hello from Flask ECS app on port 5000!")

@app.route("/health")
def health():
    app.logger.info("Health check called")
    return jsonify(status="ok"), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
