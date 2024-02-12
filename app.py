from flask import Flask, request, jsonify, abort

app = Flask(__name__)
@app.route("/webhook", methods=['POST'])
def app_():
    if request.method == "POST":
        print(request.json())
        return "success"
    else:
        abort(400)

if __name__ == "__main__":
    app.run()