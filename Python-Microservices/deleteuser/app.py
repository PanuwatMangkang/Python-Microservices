from flask import Flask, request, render_template, redirect, jsonify
import os
#pip install mysql-connector-python
import mysql.connector as mysql

# Configure MySQL connection
conn = mysql.connect(
    host="Localhost",
    user="root",
    password="12345678",
    port=3306,
    database="my_memo"
)
app = Flask(__name__)


@app.route('/delete/<email>', methods=["DELETE"])
def delete_user(email):
    cur = conn.reconnect()
    cur = conn.cursor()
    sql = "DELETE FROM memo WHERE email=%s "
    data = (email,)
    cur.execute(sql, data)
    conn.commit()
    conn.close()
    return redirect('http://localhost:5001/getuser')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5002, debug=True)