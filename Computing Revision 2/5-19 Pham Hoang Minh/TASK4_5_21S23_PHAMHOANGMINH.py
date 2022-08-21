from flask import Flask,render_template,url_for

app = Flask(__name__)





@app.route('/')
def home():
    return render_template("TASK4_6_21S23_PHAMHOANGMINH.html")




@app.route('/results',methods = ["POST"])
def search_results():
    return render_template("search_results.html")







if __name__ == ('__main__'):
    app.run(port=12345,debug = True)
