from flask import Flask,render_template,request

app = Flask(__name__)
@app.route('/')
def form():
    return render_template('index.html')

@app.route('/results',methods = ['POST'])
def data():
    email = request.form['email']
    print(email)
    








if __name__ == "__main__":
    app.run(port = 1234,debug = True)
