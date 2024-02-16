# from flask import Flask, request, jsonify, abort
# from flask_mysqldb import MySQL

# app = Flask(__name__)
# app.config['MYSQL_HOST'] ='127.0.0.1'
# app.config['MYSQL_USER'] = 'webhook'
# app.config['MYSQL_PASSWORD'] ='Jasper@1998'
# app.config['MYSQL_DATABASE'] = 'apollo_contacts'
# app.config['MYSQL_PORT'] = 3306  # Default MySQL port
# mysql = MySQL(app)
# @app.route("/webhook", methods=["POST"])
# def app_():
#     if request.method == "POST":
#         try:
#             cur = mysql.connection.cursor()
#             information = request.json
#             print(information)
            
#             people_id = information['people'][0]['id']
#             phone_numbers = information['people'][0].get('phone_numbers', [])
#             raw_number = phone_numbers[0]['raw_number'] if phone_numbers else None
            
#             insert_query = "INSERT INTO phone (id, mobile) VALUES (%s, %s)"
#             cur.execute(insert_query, (people_id, raw_number))
        
#             cur.close()
            
#             return jsonify({"message": "Data successfully inserted into MySQL database"}), 200
#         except MySQL.Error as e:
#             return jsonify({"error": str(e)}), 500
#         except KeyError as e:
#             return jsonify({"error": f"Missing key in request data: {str(e)}"}), 400
#     else:
#         abort(405)


from flask import Flask, request, jsonify, abort
import mysql.connector as my


@app.route("/webhook", methods=["POST"])
def app_():
    if request.method == "POST":
        try:
            con= my.connect(host='127.0.0.1',user='webhook',password='Jasper@1998')
            cursor=con.cursor()
            cursor.execute('USE apollo_contacts') 
            information = request.json
            print(information)
            
            people_id = information['people'][0]['id']
            phone_numbers = information['people'][0].get('phone_numbers', [])
            raw_number = phone_numbers[0]['raw_number'] if phone_numbers else None
            
            insert_query = "INSERT INTO phone (id, mobile) VALUES (%s, %s)"
            cursor.execute(insert_query, (people_id, raw_number))
        
            cursor.close()
            con.close()
            return jsonify({"message": "Data successfully inserted into MySQL database"}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500
        except KeyError as e:
            return jsonify({"error": f"Missing key in request data: {str(e)}"}), 400
    else:
        abort(405)