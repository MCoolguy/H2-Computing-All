import sqlite3
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def main():
    return render_template('index.html')

@app.route('/latecomers', methods=['GET'])
def latecomers():
    # Retrieve data from SQLite database
    with sqlite3.connect('Task4.db') as conn:
        cur = conn.cursor()
        cur.execute("""
SELECT Name, Date, Time FROM Person
INNER JOIN Record
ON Person.id = Record.visitorId
WHERE Time > '0730'
AND Type = 'entry'
AND Role = 'Student'
ORDER BY Date, Time ASC;
        """)
        result = cur.fetchall()
    # conn.close() is automatically called

    return render_template(
        'latecomer.html',
        result=result,
    )

app.run()
