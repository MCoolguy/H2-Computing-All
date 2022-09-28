import flask
from flask import Flask,render_template
import sqlite3


app = Flask(__name__)

@app.route('/')
return render_template('home.html')

@app.route('/result')
conn = sqlite3.connect('equipment.db')
cursor = conn.cursor()
templist = cursor.fetchall()

return render_template('results.html',results = results)





if __name__=="__main__":
    app.run('127.0.0.1',1234)
