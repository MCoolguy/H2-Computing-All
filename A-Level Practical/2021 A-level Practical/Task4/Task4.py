from flask import *
import sqlite3

app = Flask(__name__,template_folder = 'Task4_1_21S23')



@app.route('/')
def home():
    return render_template("home.html")


@app.route('/round1')
def round1():
    conn = sqlite3.connect('Task4.db')
    sqlcommand = '''SELECT name,score FROM competitor,scores WHERE round = 1 
                    AND competitor.id = scores.id ORDER BY scores.score DESC'''
                    
    cursor = conn.execute(sqlcommand)
    data = []
    for item in cursor:
        data.append(item)
                    
                    
    return render_template("round1.html",data=data)

@app.route('/round2')
def round2():
    conn = sqlite3.connect('Task4.db')
    sqlcommand = '''SELECT name,score FROM competitor,scores WHERE round = 2
                    AND competitor.id = scores.id ORDER BY scores.score DESC'''
                    
    cursor = conn.execute(sqlcommand)
    data = []
    for item in cursor:
        data.append(item)
                    
                    
    return render_template("round1.html",data=data)

@app.route('/round3')
def round3():
    conn = sqlite3.connect('Task4.db')
    sqlcommand = '''SELECT name,score FROM competitor,scores WHERE round = 3 
                    AND competitor.id = scores.id ORDER BY scores.score DESC'''
                    
    cursor = conn.execute(sqlcommand)
    data = []
    for item in cursor:
        data.append(item)
                    
                    
    return render_template("round1.html",data=data)

@app.route('/MeanScores')
def mean():
    conn = sqlite3.connect('Task4.db')
    sqlcommand = '''Select competitor.name as Names, SUM(scores.Score)/COUNT(scores.round) as Mean FROM
competitor,scores where competitor.id = scores.id
group by name
order by name ASC'''
                    
    cursor = conn.execute(sqlcommand)
    data = []
    for item in cursor:
        data.append(item)
                    
    
    return render_template("meanscores.html",data=data)

@app.route('/Qualifiers')
def qualifiers():
    conn = sqlite3.connect('Task4.db')
    sqlcommand = '''SELECT competitor.name as Name, sum(scores.score) as Total, 
                    SUM(scores.score)>250 as Qualified
                FROM competitor, scores
                WHERE competitor.id = scores.id 
                GROUP BY name 
                ORDER BY Qualified DESC, Total DESC'''
                    
    cursor = conn.execute(sqlcommand)
    data = []
    for item in cursor:
        if item[2]==0:
            item = (item[0],item[1],"No")
        else:
            item = (item[0],item[1],"Yes")

        data.append(item)
    return render_template("qualifiers.html",data=data)







if __name__ =='__main__':
    app.run(port =1234)