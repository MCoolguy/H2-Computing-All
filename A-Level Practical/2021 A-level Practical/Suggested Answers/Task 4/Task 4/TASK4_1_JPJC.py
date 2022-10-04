from flask import Flask, render_template

app = Flask(__name__, template_folder = "TASK4_4_JPJC") 

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/round1/')
def round1():
    import sqlite3
    db = sqlite3.connect("Task4.db")
    rows = db.execute('''SELECT competitor.name, scores.score
                      FROM competitor, scores
                      WHERE competitor.id = scores.id AND round = 1
                      ORDER BY scores.score desc''')
    data = rows.fetchall() #fetchall as a list of records
    db.close()
    return render_template('round_scores.html', rows = data, round = 1)

@app.route('/round2/')
def round2():
    import sqlite3
    db = sqlite3.connect("Task4.db")
    rows = db.execute('''SELECT competitor.name, scores.score
                      FROM competitor, scores
                      WHERE competitor.id = scores.id AND round = 2
                      ORDER BY scores.score desc''')
    data = rows.fetchall()
    db.close()
    return render_template('round_scores.html', rows = data, round = 2)

@app.route('/round3/')
def round3():
    import sqlite3
    db = sqlite3.connect("Task4.db")
    rows = db.execute('''SELECT competitor.name, scores.score
                      FROM competitor, scores
                      WHERE competitor.id = scores.id AND round = 3
                      ORDER BY scores.score desc''')
    data = rows.fetchall()
    db.close()
    return render_template('round_scores.html', rows = data, round = 3)

@app.route('/mean/')
def mean():
    import sqlite3
    db = sqlite3.connect("Task4.db")
    rows = db.execute('''SELECT competitor.name, round( round(SUM(scores.score),1)/round(COUNT(scores.score),1), 2)
                        FROM competitor, scores
                        WHERE competitor.id = scores.id
                        GROUP BY name
                        ORDER BY name ASC''')
    data = rows.fetchall()
    db.close()
    return render_template('mean.html', rows = data)

@app.route('/qualified/')
def qualified():
    import sqlite3
    db = sqlite3.connect("Task4.db")
    rows = db.execute('''SELECT competitor.name as Name, sum(scores.score) as Total, SUM(scores.score)>250 as Qualified
                        FROM competitor, scores
                        WHERE competitor.id = scores.id 
                        GROUP BY name 
                        ORDER BY Qualified DESC, Total DESC''')
    data = rows.fetchall()
    db.close()
    return render_template('qualified.html', rows = data)

if __name__ == "__main__":
    app.run(port = 5667, debug = True)

