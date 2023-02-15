from flask import Flask, jsonify
import time

app = Flask(__name__)

@app.route('/')
def index():
    time.sleep(1)
    return jsonify({"message": "Hello World"})
