import flask
from flask import Flask,render_template,request
import random


app = Flask(__name__)

@app.route('/')
def form():
    return render_template("form.html")

@app.route('/result',methods = ['POST'])
def result():
    result = ""
    playerchoice = request.form['choice']
    if playerchoice == 'gun':
        result = 'SERVER CHOSE GUN YOU TIED'
    else:
        result = 'SERVER CHOSE GUN YOU LOST'
        
    return render_template("result.html",result = result)
    
    
        
    


if __name__ == "__main__":
    app.run(port = 4567,debug=True)