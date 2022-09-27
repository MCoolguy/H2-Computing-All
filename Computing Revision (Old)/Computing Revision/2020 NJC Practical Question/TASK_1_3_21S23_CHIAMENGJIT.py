import flask
from flask import request, render_template
import sqlite3

def departments():
    conn = sqlite3.connect("schools.db")
    cur = conn.cursor()
    cur.execute("SELECT DISTINCT Department FROM staff ORDER BY Department ASC")
    rows = cur.fetchall()
    department = []
    for row in rows:
        department.append(row[0])
    conn.close()
    return department

def schools():
    conn = sqlite3.connect("schools.db")
    cur = conn.cursor()
    cur.execute("SELECT DISTINCT Name FROM schools ORDER BY Name ASC")
    rows = cur.fetchall()
    schools = []
    for row in rows:
        schools.append(row[0])
    conn.close()
    return schools

def search_html(school, department):
    connection = sqlite3.connect("schools.db")
    sql_statement = """
                    SELECT schools.Name, staff.Name, staff.Department, staff.Contact, schools.Address
                    FROM schools, staff
                    WHERE staff.SchoolCode = schools.SchoolCode AND schools.Name LIKE ? AND staff.Department LIKE ?
                    """

    cur = connection.cursor()
    cur.execute(sql_statement,('%'+school+'%',department))
    rows = cur.fetchall()
    results = []
    for row in rows:
        results.append(row)
    
    return results
    

app = flask.Flask(__name__)

@app.route('/') #the items in the brackets create the links inside

def home():
    school = schools()
    print(school)
    return render_template('home.html', schools = school)



@app.route('/result', methods = ['POST'])
def generate_report():
    if 'department' in request.form and 'school' in request.form:
        #list to contain department and school
        lst = []
        lst.append(request.form['department'])
        lst.append(request.form['school'])
    department = lst[0]
    school = lst[1]
    result = search_html(school, department)
    return render_template('results.html', result = result)


if __name__ == '__main__':
    app.run(port = 12358, debug = True)
