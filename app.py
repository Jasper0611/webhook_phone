from flask import Flask, request, jsonify, abort
import mysql.connector as my

con= my.connect(host='localhost',user='root',password='Jasper@1998')
cursor=con.cursor()
cursor.execute('USE apollo_contacts') 

app = Flask(__name__)
@app.route("/webhook", methods=['POST'])
def app_():
    if request.method == "POST":
        information = request.json
        people_id = information['people'][0]['id']
        
        # Check if 'phone_numbers' list is not empty
        phone_numbers = information['people'][0].get('phone_numbers', [])
        if phone_numbers:
            raw_number = phone_numbers[0].get('raw_number', None)
        else:
            raw_number = None
        
        insert_query = "INSERT INTO phone (id, mobile) VALUES (%s, %s)"
        cursor.execute(insert_query, (people_id, raw_number))
        con.commit()
        return "success"
    else:
        abort(400)
