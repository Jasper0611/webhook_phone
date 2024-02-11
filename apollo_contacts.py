from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route("/webhook", methods=['POST'])
def app_():
    data = request.get_json()
    print(data)
    return 'Success'