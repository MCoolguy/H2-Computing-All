#Program 6 - update.py
import pymongo
client = pymongo.MongoClient("127.0.0.1", 27017)
db = client.get_database("entertainment")
if "better movies" in db.collection_names():
    db.drop_collection("better movies")
#print("existing collections are: ", db.collection_names())

col = db.get_collection("better movies")

col.insert_one({"_id":1, "title":"Johnny Maths", "genre":"comedy"})
col.insert_one({"title":"Star Walls", "genre":"science fiction"})
col.insert_one({"title":"Detection"}) #no genre
list_to_add = []
list_to_add.append({"title":"Badman", "genre":"adventure", "year":2015})
list_to_add.append({"title":"Averages 2", "genre":["adventure","comedy"], "year":2017})
list_to_add.append({"title":"Averages", "genre":["comedy","adventure"], "year":2017})
list_to_add.append({"title":"Octopus Man", "genre":"adventure", "year":2017})
list_to_add.append({"title":"Fantastic Bees", "genre":"adventure", "year":2018})
list_to_add.append({"title":"Underground", "genre":"comedy", "year":2014})
#list_to_add.append({"title":"Test1", "genre":["adventure"]})
col.insert_many(list_to_add)

#search = {'year':{'$gt':2016}}
#update = {'$set':{'year':2015}}
#col.update_one(search, update)
#col.update_one(search, update)

#search = {'year':{'$eq':2018}}
#update = {'$unset':{'year':0}}
#col.update_many(search, update)
#search = {'year':{'$exists':0}}
#update = {'$set' :{'year' :2019}}
#col.update_many(search, update)

#query= {'$and':[{'title':{'$eq': "Fantastic Bees"}} , {'genre':{'$eq': "adventure"}}]}
#projection = {'title' :1, 'genre' : 1, 'year' :1, "_id" : 0}
#result = col.find(query,projection)
#for i in result:
#    print(i)

#result = col.find()
#print("existing collections are: ", db.collection_names())
#print("All documents in new movies collection:")
#for document in result:
#    print(document)
result = col.find({'$or':[{"genre":{'$eq':["comedy","adventure"]}},{"genre":{'$eq':["adventure","comedy"]}}]})
for doc in result:
    print(doc)


client.close()
