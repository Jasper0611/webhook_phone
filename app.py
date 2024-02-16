from flask import Flask, request, jsonify, abort
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] ='localhost'
app.config['MYSQL_USER'] = 'webhook'
app.config['MYSQL_PASSWORD'] ='Jasper@1998'
app.config['MYSQL_DATABASE'] = 'apollo_contacts'
mysql = MySQL(app)
# Connect to MySQL server
# cursor  = my.connect(host='127.0.0.1', user='webhook', password='Jasper@1998', database='apollo_contacts')
# cursor = con.cursor()

@app.route("/webhook", methods=["GET", "POST"])
def app_():
    if request.method == "GET":
        # Handle GET request (if needed)
        return "This endpoint only accepts POST requests."
    elif request.method == "POST":
        conn = mysql.connection
        cur = conn.cursor()
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
            
            insert_query = "INSERT INTO phone (id, mobile) VALUES (%s, %s)"
            cur.execute(insert_query, (people_id, raw_number))
            conn.commit()
            return "Data successfully inserted into MySQL database."
        except Exception as e:
            return f"Error: {str(e)}"
    else:
        # Return a 405 Method Not Allowed error if the request method is not GET or POST
        abort(405)

