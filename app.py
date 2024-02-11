from flask import Flask, request, jsonify
import requests
import logging

app = Flask(__name__)
logging.basicConfig(filename='webhook.log', level=logging.INFO)
@app.route("/webhook", methods=['POST'])
def app_():
    data = request.get_json()
    logging.info(f'Received data: {data}')
    return 'Success'