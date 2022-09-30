import sqlite3
from flask import Flask, render_template, request

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

@app.route('/add', methods=['GET'])
def add():
    """Display web form to add entry"""
    return render_template('add.html')

@app.route('/status', methods=['POST'])
def submit():
    """Display status of entry/exit add"""
    status = 'success'

    # Get form data from request
    record = {}
    record['Date'] = '2022-10-05'
    record['Time'] = '0722'
    record['Type'] = request.form['direction']
    record['visitorId'] = request.form['visitorId']

    # Validation step
    if record['Type'] not in ('entry', 'exit'):
        status = 'failure'
    
    # Insert into database
    if status == 'success':
        try:
            with sqlite3.connect('Task4.db') as conn:
                cur = conn.cursor()
                cur.execute("""
    INSERT INTO Record (Date, Time, Type, visitorId)
    VALUES(?, ?, ?, ?);
                    """,
                    (
                        record['Date'],
                        record['Time'],
                        record['Type'],
                        record['visitorId']
                    )
                )
                conn.commit()
            # conn.close() is automatically called
        except:
            status = 'failure'

    # Display status in response
    return render_template(
        'status.html',
        status=status,
        record=record,
    )

app.run()
