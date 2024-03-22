from flask import Flask, request, render_template, redirect, jsonify
import os
#pip install mysql-connector-python
import mysql.connector as mysql

app = Flask(__name__)

# Configure MySQL connection
conn = mysql.connect(
    host="Localhost",
    user="root",
    password="12345678",
    port=3306,
    database="my_memo"
)
app = Flask(__name__)

@app.route('/getuser/v1/<idmemo>', methods=["GET"])
def get_user(idmemo):
    cur = conn.reconnect()
    sql = "SELECT idmemo, firstname, lastname, email "
    sql += " FROM memo WHERE idmemo=%s ORDER BY firstname"
    data = (idmemo,)
    cur = conn.cursor()
    cur.execute(sql, data)
    record = cur.fetchone()
    conn.close()
    return jsonify(record)

@app.route('/getuser', methods=["GET"])
def get_user_all():
    cur = conn.reconnect()
    sql = "SELECT idmemo, firstname, lastname, email "
    sql += " FROM memo ORDER BY firstname"
    cur = conn.cursor()
    cur.execute(sql)
    records = cur.fetchall()
    conn.close()
    return jsonify(records)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)