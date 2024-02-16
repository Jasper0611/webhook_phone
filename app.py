from flask import Flask, request, jsonify, abort
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] ='localhost'
app.config['MYSQL_USER'] = 'webhook'
app.config['MYSQL_PASSWORD'] ='Jasper@1998'
app.config['MYSQL_DATABASE'] = 'apollo_contacts'
app.config['MYSQL_PORT'] = 3306  # Default MySQL port
app.config['MYSQL_UNIX_SOCKET'] = None  # Disable Unix socket
mysql = MySQL(app)
@app.route("/webhook", methods=["POST"])
def app_():
    if request.method == "POST":
        try:
            conn = mysql.connection
            cur = conn.cursor()

            information = request.json
            print(information)
            
            people_id = information['people'][0]['id']
            phone_numbers = information['people'][0].get('phone_numbers', [])
            raw_number = phone_numbers[0]['raw_number'] if phone_numbers else None
            
            insert_query = "INSERT INTO phone (id, mobile) VALUES (%s, %s)"
            cur.execute(insert_query, (people_id, raw_number))
            conn.commit()
            
            cur.close()
            conn.close()
            
            return jsonify({"message": "Data successfully inserted into MySQL database"}), 200
        except mysql.connector.Error as e:
            return jsonify({"error": str(e)}), 500
        except KeyError as e:
            return jsonify({"error": f"Missing key in request data: {str(e)}"}), 400
    else:
        abort(405)