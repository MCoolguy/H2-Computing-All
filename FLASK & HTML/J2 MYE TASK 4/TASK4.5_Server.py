import flask
from flask import Flask,render_template,request
import sqlite3

app  = Flask(__name__)

@app.route('/')
def form():
    return render_template('userform.html')

@app.route('/results',methods = ['POST'])
def results():
    schoolname = request.form['schoolname']
    con = sqlite3.connect("schools.db")
    cursor = con.execute("SELECT School.Name,School.Zone,School.Level,School.YearsOfStudy,Subject.SubjectName FROM School,Subject \
                     WHERE School.SchoolID = Subject.SchoolID AND School.Name = ? ",(schoolname,))

    row = cursor.fetchall()
    name = row[1][0]
    zone = row[1][1]
    level = row[1][2]
    yos = row[1][3]
    subj = []
    for rows in row:
        subj.append(rows[4])

        
    return render_template("results.html",name = name, zone = zone,level = level, yearofstudy = yos,offered=subj)










if __name__ == "__main__":
    app.run(port=1234,debug = True)