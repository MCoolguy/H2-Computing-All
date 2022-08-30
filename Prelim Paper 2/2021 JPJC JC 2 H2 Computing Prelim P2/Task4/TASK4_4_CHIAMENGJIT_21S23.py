import pymongo
from flask import render_template, request
import flask
#from TASK4_CHIAMENGJIT_21S23 import load_collection, database_exist
#task 4.4, to receive input 'brand' from html web browser
#return html document to display ordered list of mobile phones sorted by price
#mongodb+srv://mcoolguy:minhmoc123@mongoforjpjc.nsdccjd.mongodb.net/?retryWrites=true&w=majority
def load_collection():
    global client
    client = pymongo.MongoClient("mongodb+srv://mcoolguy:minhmoc123@mongoforjpjc.nsdccjd.mongodb.net/?retryWrites=true&w=majority")
    db = client.get_database("jp_mobile")
    coll = db.get_collection("phone")
    return coll


app = flask.Flask(__name__)

@app.route('/') #home page
def home():
    return render_template("TASK4_4_CHIAMENGJIT_21S23_08.html")


@app.route('/result', methods = ["GET"])
def result():
    if "brand" in request.args:
        brand = request.args["brand"]
        #retrieving the brand from mongodb now
        coll = load_collection()
        query = {"brand": {'$eq':brand} }
        #query = {"$text": {'$search':brand } }
        cur = list(coll.find(query,{'_id':0,'brand':1,'model':1,'colour':1,
                                             'price':1} 
                 ).sort("price", -1)
                   )
        
        lst = []
        for item in cur:
            lst.append([item["brand"],item["model"],item["colour"],item["price"]])
        client.close()
        
    return render_template("result.html", lst_of_phones = lst)


if __name__ == "__main__":
    app.run(port = 1260, debug = True)
