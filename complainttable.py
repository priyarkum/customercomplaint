import sqlite3
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search_result',methods=["GET"])
def display_result():
     
    c_id=request.args.get("c_id")
        # open the connection to the database
    conn = sqlite3.connect('complaint.db')
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute(f"select * from customerdetail JOIN bankdetail ON customerdetail.complaint_ID=bankdetail.complaint_ID WHERE customerdetail.complaint_ID='{c_id}' ")
    rows = cur.fetchall()
    conn.close()
    return render_template('output.html', rows=rows)