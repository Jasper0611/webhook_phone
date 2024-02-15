from flask import Flask, request, jsonify, abort
import mysql.connector as my

app = Flask(__name__)

# Connect to MySQL server
con = my.connect(host='3.213.221.109', user='coe_n8nuser', password='7kbn21CLh5JQ', database='TCS_datateam')
cursor = con.cursor()

@app.route("/webhook", methods=["GET", "POST"])
def app_():
    if request.method == "GET":
        # Handle GET request (if needed)
        return "This endpoint only accepts POST requests."
    elif request.method == "POST":
        # Handle POST request
        information = request.json
        print(information)
        
        # Insert data into MySQL table
        try:
            people_id = information['people'][0]['id']
            phone_numbers = information['people'][0].get('phone_numbers', [])
            if phone_numbers:
                raw_number = phone_numbers[0].get('raw_number', None)
            else:
                raw_number = None
            
            insert_query = "INSERT INTO hot_leads_phone (id, mobile) VALUES (%s, %s)"
            cursor.execute(insert_query, (people_id, raw_number))
            con.commit()
            return "Data successfully inserted into MySQL database."
        except Exception as e:
            return f"Error: {str(e)}"
    else:
        # Return a 405 Method Not Allowed error if the request method is not GET or POST
        abort(405)

