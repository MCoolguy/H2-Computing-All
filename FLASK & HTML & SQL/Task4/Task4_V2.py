from flask import Flask, request, render_template
import sqlite3
import datetime as dt

app = Flask(__name__)

@app.route("/<location_id>")
def ret_form(location_id): #loading of the check-in page with dynamic location ID
       return render_template("checkin.html",location_id = location_id)

@app.route("/check_in/<location_id>",methods=["POST"])
def check_in(location_id): ## triggered by user clicking on the "Check In" button in html
    try:
        con = sqlite3.connect("EntryDB_.DB")
        con.row_factory = sqlite3.Row
        
        today = dt.datetime.now()           

        #Qn req on date: YYMMDD
        #Qn req on time: HHMM (24Hour)
        date = f"{today:%y%m%d}"
        time = f"{today:%H%M}"
        
        nric = request.form['NRIC']
        name = request.form['Name']
        contact = request.form['Contact']
        con.execute("INSERT INTO Visitor (NRIC,LocationID,Name,Contact, Date,TimeIn) VALUES(?,?,?,?,?,?)",
                    (nric ,location_id, name, contact, date, time))
        con.commit()
        
    except sqlite3.Error as ex:    
        print(ex)
    con.close()
    return f"Please clicked on link to check out <a href='/check_out/{location_id}/{nric}'> Check Out</a>"

@app.route("/check_out/<location_id>/<nric>")
def check_out(location_id, nric): #triggered when user clicks on the URL to Check out.
                                  #with the locationID and NRIC of the user specified in the url 
    try:
        con = sqlite3.connect("EntryDB_.DB")
        con.row_factory = sqlite3.Row

        today = dt.datetime.now()
        date = f"{today:%y%m%d}" #assuming that visitor will not stay overnight at the premise
        time = f"{today:%H%M}"

        con.execute("UPDATE Visitor SET TimeOut=? WHERE NRIC=? AND LocationID=? AND Date=?",
                    (time, nric ,location_id, date))
        con.commit()
        
    except sqlite3.Error as ex:
        print(ex)
    con.close()
    return f"{nric} checked out at {location_id}"


if __name__ == '__main__':
    app.run(port = 5000, debug = True)
