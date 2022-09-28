import flask
from flask import Flask,render_template,request
import sqlite3


app = Flask(__name__)

@app.route('/')
def form():
    return render_template("home.html")

@app.route('/results',methods = ['POST'])
def results():
    location = request.form['location']
    conn = sqlite3.connect("equipment.db")
    cursor = conn.execute("SELECT Device.SerialNumber,Device.Type FROM DEVICE WHERE Device.Location =?",(location,))

    row = cursor.fetchall()
    serialnumbers = []
    types = []
    for count in range(len(row)-1):
        serialnumbers.append(row[count][0])
        types.append(row[count][1])
        
        



if __name__=="__main__":
    app.run('127.0.0.1',1234)
