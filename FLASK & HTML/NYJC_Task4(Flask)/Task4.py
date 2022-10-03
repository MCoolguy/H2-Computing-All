import flask
from flask import Flask, render_template,url_for,request
import sqlite3 



app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")


@app.route('/latecomers')
def latecomers():

    conn = sqlite3.connect("Task4.db")
    cursor = conn.cursor()
    cursor.execute("SELECT Name, Date, Time FROM Person INNER JOIN Record ON Person.id = Record.visitorId WHERE Time > '0730' AND Type = 'entry' AND Role = 'Student' ORDER BY Date ASC, Time ASC;")

    data = cursor.fetchall()
    headers = ('Name','Date','Time')
    
    return render_template("latecomers.html",data=data,headers = headers)

@app.route('/addrecordform')
def addrecordform():
    return render_template("addrecordform.html")


@app.route('/addrecord',methods = ['POST'])
def addrecord():
    visitorID = request.form['visitorID']
    direction = request.form['direction']
    time = "0722"
    date = "2022-10-05"
    conn = sqlite3.connect("Task4.db")
    status = 'success'
    headers = ('visitorID','direction','time','date')
    if visitorID.isdigit() and int(visitorID)<7:
        conn.execute("INSERT INTO Record('visitorId','Type','Date','Time')VALUES(?,?,?,?)",(visitorID,direction,date,time))
        conn.commit()
    else:
        status = 'failure'
    
    
    
    
    return render_template('addrecord.html',status=status,visitorID=visitorID,direction=direction,time=time,date=date,headers = headers)







if __name__ == "__main__":
    app.run(port=6969,debug=True)