#Program 2 - insert.py

def deleteCol(colName):
    db.drop_collection(colName)
    print("Remaining Collections:", db.collection_names())
    
def deleteDB(dbName):
    client.drop_database(dbName)

def disconnectMongoDB():
    client.close()

def displayAll(results):
##    projection = {'_id':0} #show all except '_id'
##    results = col.find({},projection)
    count = 0
    print("------------------------------------------------------")
    print(("{0:25}{1:30}").format("Title", "Genre"))
    print("------------------------------------------------------")
    for doc in results:
        title = str(doc.get("title"))
        genre = str(doc.get("genre"))
        print(("{0:25}{1:30}").format(title, genre))
        count = count + 1
    print("-------------------------------------------------------")
    print("Total no. of books:", count)

#------------------------main program--------------------------------
import pymongo
import datetime
client = pymongo.MongoClient("127.0.0.1", 27017)

print("---------------Welcome to JPJC Movies DB----------------")
dbName = "entertainment"
db = client.get_database(dbName)
colName = "movies"
col = db.get_collection(colName)

deleteCol(colName)

#insert document one by one
col.insert_one({"_id":1, "title":"Johnny Maths", "genre":"comedy"})
col.insert_one({"title":"Star Walls", "genre":"science fiction"})
col.insert_one({"title":"Detection"}) #no genre

#insert multiple documents 
list_to_add = []
list_to_add.append({"title":"Badman", "genre":"adventure", "year":2015}) 
list_to_add.append({"title":"Averages", "genre":["science fiction","adventure"], "year":2017})
list_to_add.append({"title":"Octopus Man", "genre":"adventure", "year":2017})
list_to_add.append({"title":"Fantastic Bees", "genre":"adventure", "year":2018})
list_to_add.append({"title":"Underground", "genre":"horror", "year":2014})
col.insert_many(list_to_add)


#Read Operations
print("Result 1")
result_1 = col.find({'genre':{'$in':['adventure', 'science fiction']}}) #returns Star Walls, Averages, Octopus Man, Fantastic Bees
displayAll(result_1)

print("Result 2")
query2 = {'genre': {'$exists':False}}
result_2 = col.find(query2)
displayAll(result_2)

print("Result 3")
result_3 = col.find({'year':{'$eq':2017}})
displayAll(result_3)

print("Result 4")
result_4 = col.find({'year': 2017})
displayAll(result_4)

print("Result 5")
result_5 = col.find({'genre':{ '$not':{'$in':['adventure','comedy']}}})
displayAll(result_5)

print("Result 6")
result_6 = col.find({'genre': { '$nin' :['adventure','comedy']}})
displayAll(result_6)


query7 = {'year': {'$exists':True}} #to only consider doc with year field
result_7 = col.find(query7)

print("All movies with year given:")
thisYear = datetime.date.today().year
for document in result_7:
    movieYear = int(document.get('year'))
    print(thisYear)
    print(" - Title:", document.get('title'), ", No. of year(s) since release:", thisYear-movieYear)




