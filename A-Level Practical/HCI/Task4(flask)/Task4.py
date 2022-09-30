import flask
from flask import Flask,render_template,url_for,request
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

@app.route('/addrecordform')
def addrecordform():
    return render_template("addrecordform.html")

@app.route('/addrecord',methods = ['POST'])
def addrecord():
    name = request.form['name']
    gender = request.form['gender']
    studentid = request.form['studentid']
    weight = request.form['weight']
    height = request.form['height']
    
    
    
    headers = ('name','gender','studentid','weight','height')
    
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    studentIDs = []
    cursor.execute("SELECT StudentID from StudentHealthRecord")
    studentIDs = cursor.fetchall()
    if (int(studentid),) in studentIDs:
        return "StudentID already exists in database"

    conn.execute("INSERT INTO Student(Name,Gender) VALUES(?,?)",(name,gender))
    conn.execute("INSERT INTO StudentHealthRecord(StudentID,Weight,Height) VALUES(?,?,?)",(studentid,weight,height))
    conn.commit()
    return render_template('addrecord.html',headers = headers,name=name,gender=gender,studentid=studentid,height=height,weight=weight)

    







if __name__ == '__main__':
    app.run(port=6789,debug=True)