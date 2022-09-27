import sqlite3
import flask
from flask import render_template
from flask import request, url_for

app= flask.Flask(__name__)
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/help', methods = ['POST'])
def search():
    connection = sqlite3.connect("schools.db")
    cursor = connection.execute("SELECT SchoolCode,Name,Address FROM school")
    cursor2 = connection.execute("SELECT SchoolCode,Department,Name,Contact FROM staff")
    rows = cursor.fetchall()
    rows2 = cursor2.fetchall()
    listofstaff = []
    listofschools = []
    for row in rows:
        listofschools.append(row)
    for row in rows2:
        listofstaff.append(row)
    #################################### Retrieving data from database
    name = request.form["schoolname"]
    result = [i for i in listofschools if name in i]
    ##################################################
    department =request.form["department"]
    listofschools = list(listofschools)
    result2 = []
    departmentsearch = department
    for i in range(20):
        if departmentsearch == listofstaff[i][1]:
            result2.append(listofstaff[i])
    result2len = len(result2)
    for n in range(3):
        code = listofschools[n][0]
        staffname = listofschools[n][1]
        address = listofschools[n][2]

        for m in range(result2len):
            if int(code) ==result2[m][0]:
                schoolname = staffname

    cursor = [name, department]
    return render_template('search.html', cursor = cursor)

if __name__ == '__main__':
    app.run()




connection.close()
