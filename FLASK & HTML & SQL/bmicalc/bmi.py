import flask
from flask import Flask,render_template,request

app = Flask(__name__)
@app.route('/')
def home():
    return render_template("form.html")

@app.route('/results', methods = ['POST'])
def results():
    height = float(request.form['height'])
    weight = float(request.form['weight'])
    bmi = round(weight/(height**2),1)
    return render_template('results.html',bmi = bmi)










if __name__ == "__main__":
    app.run(port=1234,debug =True)