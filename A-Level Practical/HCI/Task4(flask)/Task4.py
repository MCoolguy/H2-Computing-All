import flask
from flask import Flask,render_template,url_for
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("Task4_1.html")

@app.route('/records')
def records():
    conn  = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute("SELECT Name,Gender,Weight,Height FROM Student LEFT OUTER JOIN StudentHealthRecord ON \
        Student.StudentID = StudentHealthRecord.StudentID\
        ORDER BY Gender ASC,Name DESC")

    data = cursor.fetchall()
    headers = ('Name','Gender','Weight','Height')
    
    return render_template('records.html',headers = headers,data=data)

@app.route('/stats')
def stats():
    headers = ('Attributes','Male','Female')
    conn  = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute("SELECT SUM(StudentHealthRecord.Weight)/count(StudentHealthRecord.Weight) \
        FROM StudentHealthRecord,Student Where StudentHealthRecord.StudentID = Student.StudentID AND Student.Gender='M'")
    averageMweight = round(cursor.fetchone()[0],2)
    
    cursor.execute("SELECT SUM(StudentHealthRecord.Height)/count(StudentHealthRecord.Height) \
        FROM StudentHealthRecord,Student Where StudentHealthRecord.StudentID = Student.StudentID AND Student.Gender='M'")
    averageMheight = round(cursor.fetchone()[0],2)
    
    cursor.execute("SELECT SUM(StudentHealthRecord.Weight)/count(StudentHealthRecord.Weight) \
        FROM StudentHealthRecord,Student Where StudentHealthRecord.StudentID = Student.StudentID AND Student.Gender='F'")
    averageFweight = round(cursor.fetchone()[0],2)
    
    cursor.execute("SELECT SUM(StudentHealthRecord.Height)/count(StudentHealthRecord.Height) \
        FROM StudentHealthRecord,Student Where StudentHealthRecord.StudentID = Student.StudentID AND Student.Gender='F'")
    averageFheight = round(cursor.fetchone()[0],2)
    
    cursor.execute("SELECT count(*) FROM Student WHERE Student.Gender ='F'")
    femaleNo = cursor.fetchone()[0]
    
    cursor.execute("SELECT count(*) FROM Student WHERE Student.Gender ='M'")
    maleNo = cursor.fetchone()[0]
    
    return render_template("stats.html",headers = headers,averageMweight = averageMweight,averageFweight = averageFweight,averageMheight=averageMheight,averageFheight=averageFheight,femaleNo=femaleNo,maleNo=maleNo)

@app.route('/addrecord')
def addrecord():
    return render_template("addrecord.html")





if __name__ == '__main__':
    app.run(port=6789,debug=True)