import flask
import sqlite3
app = flask.Flask(__name__)

@app.route('/')
def form():
    return flask.render_template('form.html')

@app.route('/submit', methods=["POST"])
def generate():
    submission = flask.request.form['button']
    if submission == 'Generate Report': #Generate Report Button Chosen
        data = report()
        return flask.render_template('table.html', data=data)
    else: #Submit button chosen
        insert(flask.request.form)
        return 'Data Inserted'

# Inserting into database
DATABASE = '../register.db'
def refresh():
    pass
    
def insert(data):
   pass

def report():
    pass

#-----main program----
refresh()
app.run('0.0.0.0', 5000, debug=True)
