from flask import Flask, request, render_template, redirect, jsonify
import os
#pip install mysql-connector-python
import mysql.connector as mysql

conn = mysql.connect(
    host="Localhost",
    user="root",
    password="12345678",
    port=3306,
    database="my_memo"
)
app = Flask(__name__)


@app.route('/adduser', methods=["GET"])
def add_newuser():
    return render_template('add_user.html')

@app.route('/adduser_todb', methods=["POST"])
def adduser_todb():
    cur = conn.reconnect()

    firstname = request.form.get('firstname')
    lastname = request.form.get('lastname')
    email = request.form.get('email')

    sql = "INSERT INTO my_memo.memo (firstname, lastname, email) VALUES (%s, %s, %s)"
    #sql += "VALUES(?,?,?)"
    data = (firstname, lastname, email)

    cur = conn.cursor()
    cur.execute(sql,data)
    conn.commit() #Order the server to do it
    conn.close()
    return redirect('http://localhost:5001/getuser')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5003, debug=True)