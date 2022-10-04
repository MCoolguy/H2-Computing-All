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
    data = []
    headings = ('serialnumber','type')
    for count in range(len(row)):
        data.append([row[count][0],row[count][1]])

        
    return render_template('results.html',headings = headings,data = data)
        



if __name__=="__main__":
    app.run('127.0.0.1',1234)
