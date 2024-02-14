from flask import Flask, request, jsonify, abort, render_template

app = Flask(__name__)

@app.route("/webhook", methods=["GET", "POST"])
def app_():
    if request.method == "GET":
        # Handle GET request (if needed)
        return "This endpoint only accepts POST requests."
    elif request.method == "POST":
        # Handle POST request
        information = request.json
        print(information)
        # Render a template with the JSON data
        print(information)
        return render_template("webhook_data.html", data=information)
    else:
        # Return a 405 Method Not Allowed error if the request method is not GET or POST
        abort(405)
