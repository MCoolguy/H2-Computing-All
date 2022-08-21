import sqlite3
import flask
from flask import render_template
from flask import request, url_for

app= flask.Flask(__name__)
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/help',methods = ["POST"])
def search():
    data = request.form
    Name = data["schoolname"]
    Department = data["department"]
    connection = sqlite3.connect('schools.db')
    sql = """
    SELECT school.Name, staff.Department, staff.contact, school.Address
    FROM school , staff 
    WHERE school.Name LIKE ? AND staff.Department = ?
    AND school.SchoolCode = staff.SchoolCode;
    """
    cursor = connection.execute(sql,('%'+Name+'%'+Department)).fetchall()
    connection.commit()
    connection.close()

    return render_template("search.html" ,cursor = cursor)

if __name__ == '__main__':
    app.run(port=5001,debug =True)
