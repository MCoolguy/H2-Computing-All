#Program 6 - update.py
def display():
    result = col.find()
    print("All documents in movies collection:")
    for document in result:
        print(document)
        
def insert():
    #insert docs into collection, movies
    col = db.get_collection("movies")
    col.insert_one({"_id":1, "title":"Johnny Maths", "genre":"comedy"})
    col.insert_one({"title":"Star Walls", "genre":"science fiction"})
    col.insert_one({"title":"Detection"}) #no genre
    list_to_add = []
    list_to_add.append({"title":"Badman", "genre":"adventure", "year":2015}) 
    list_to_add.append({"title":"Averages", "genre":["science fiction","adventure"], "year":2017})
    list_to_add.append({"title":"Octopus Man", "genre":"adventure", "year":2017})
    list_to_add.append({"title":"Fantastic Bees", "genre":"adventure", "year":2018})
    list_to_add.append({"title":"Underground", "genre":"horror", "year":2014})
    col.insert_many(list_to_add)
    display()
    
def one():
    #updating 2015 to the 'year' field of the first returned document where 'year' > 2016 
    search = {'year':{'$gt':2016}}
    update = {'$set':{'year':2015}}
    col.update_one(search, update)

def two():
    #updating 2015 to the 'year' field of all documents where 'year' > 2016 
    col.update_many(search, update)

def three():
    #removing the 'year' field in documents that have 2018 assigned to 'year'  
    search = {'year':{'$eq':2018}}
    update = {'$unset':{'year':0}}
    col.update_many(search, update)

def four():
    #assign field 'year' with value 2022 to documents that do not have 'year' field
    search = { 'year' : {'$exists': False }}
    search = { 'year' : {'$exists': 0 }}
    update = { '$set' : {'year': 2022} }
    col.update_many(search, update)

#main program
import pymongo
client = pymongo.MongoClient("127.0.0.1", 27017)

db = client.get_database("entertainment")

#check if "movies" exists. if so, remove collection, movies
collections = db.collection_names()
print("collections:", collections)
if "movies" in collections:
    db.drop_collection("movies")
    collections = db.collection_names()
print("collections:", collections)


client.close()
