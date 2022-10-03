import sqlite3

def departments():
    conn = sqlite3.connect("schools.db")
    cur = conn.cursor()
    cur.execute("SELECT DISTINCT Department FROM staff ORDER BY Department ASC")
    rows = cur.fetchall()
    department = []
    for row in rows:
        department.append(row[0])
    return department
