import sqlite3
from flask import Flask,render_template,request
import datetime as dt

#Task 4.1
def CreateTable():
    connection = sqlite3.connect("EntryDB.db")
    file = open("TASK4_1.sql",'r')
    sqlfile = file.read()
    file.close()
    #print(sql)
    sqlcommands = sqlfile.split(';') #commands are split by ';'
    #print(sqlcommands)
    for command in sqlcommands:
        #print(command)
        connection.execute(command) 
    
    connection.close()
    
def importdata():
    file = open("LOCATIONS.csv","r")
    file.readline()
    locationslist = []
    for line in file:
        LocationID,Name,Address,URL = line.strip().split(',')
        locationslist.append((LocationID,Name,Address,URL))
    connection = sqlite3.connect("EntryDB.db")
    for item in locationslist:
        print(item)
        connection.execute("INSERT INTO Location('LocationID','Name','Address','URL')\
            VALUES(?,?,?,?)",item)
        connection.execute("COMMIT")
        connection.commit()
    connection.close()
    
    file.close()
      
CreateTable()
importdata()

#Task 4.2

app = Flask(__name__)

@app.route('/<location_id>')
def form(location_id):
    return render_template("htmltest.html",location_id = location_id)

@app.route('/check_in/<location_id>',methods = ["POST"])
def check_in(location_id):
    con = sqlite3.connect("EntryDB.db")
    
    today = dt.datetime.now()
    date = f"{today:%y%m%d}"
    time = f"{today:%H%M}"
    
    nric = request.form['NRIC']
    name = request.form['Name']
    contact = request.form['Contact']
    con.execute("INSERT INTO Visitor (NRIC,LocationID,Name,Contact,Date,TimeIn) VALUES (?,?,?,?,?,?)",(nric,location_id,name,contact,date,time))
    con.commit()
    
    return f"Please click on link to check out <a href='/check_out/{location_id}/{nric}'> Check out</a>"
    
@app.route('/check_out/<location_id>/<nric>')
def check_out(location_id,nric):
    con = sqlite3.connect("EntryDB.db")
    
    today = dt.datetime.now()
    date = f"{today:%y%m%d}"
    time = f"{today:%H%M}"
    
    con.execute("UPDATE Visitor SET TimeOut = ? WHERE NRIC =? AND LocationID=? AND Date =? ",(time,nric,location_id,date))
    con.commit()
    
    return f"{nric} checked out of {location_id}"

if __name__ =="__main__":
    app.run(port=5000,debug =True)