from flask import *
app = Flask(__name__)

@app.route('/')

def home():
    return render_template("index.html")

@app.route('/calculate',methods = ["POST"])

def calculate():
    data = request.form
    h = float(data["height"])
    w = float(data["weight"])

    bmi = round(w/(h**2))

    return render_template("viewcalc.html",bmi = bmi)

if __name__ == "__main__":
    app.run(port=1234, debug =True)

    
