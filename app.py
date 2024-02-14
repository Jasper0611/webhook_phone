from flask import Flask, request, jsonify, abort

app = Flask(__name__)
@app.route("/webhook", methods=["POST"])
def app_():
    if methods=="POST":
        information = request.json
        print(information)
        return "success"


