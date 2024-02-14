from flask import Flask, request, jsonify, abort, Response
import csv

app = Flask(__name__)

@app.route("/webhook", methods=['POST'])
def app_():
    if request.method == "POST":
        information = request.json
        
        # Check if 'phone_numbers' list is not empty
        phone_numbers = information['people'][0].get('phone_numbers', [])
        if phone_numbers:
            raw_number = phone_numbers[0].get('raw_number', None)
        else:
            raw_number = None
        
        people_id = information['people'][0]['id']
        
        # Prepare CSV data
        csv_data = f"id,mobile\n{people_id},{raw_number}\n"

        # Send CSV file as response
        return Response(
            csv_data,
            mimetype="text/csv",
            headers={"Content-disposition": "attachment; filename=Wehbook_testcontacts.csv"}
        )
    else:
        abort(400)