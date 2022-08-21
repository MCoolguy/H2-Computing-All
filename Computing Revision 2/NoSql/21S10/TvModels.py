

def dropCollections():
    db.drop_collection("TvModels")

def insertModels():
    col.insert ([
                { 'name': "Alice", 'age': 25, 'tags': ["outgoing", "family"], 'dim_in': [ 28,22,26 ] },
                { 'name': "Belle", 'age': 31, 'tags': ["formal", "family", "plain"], 'dim_in': [ 32,26,29 ]},
                { 'name': "Cindy", 'age': 13, 'tags': ["family", "formal"], 'dim_in': [ 19,18,17 ] },
                { 'name': "Daisy", 'age': 75, 'tags': ["healthcare", "food"], 'dim_in': [ 38,40,43 ] },
                { 'name': "Eleanor", 'age': 65, 'tags': ["food", "sports"], 'dim_in': [ 36,37,38 ] },
                { 'name': "Fiona", 'age': 47, 'tags': ["formal", "family"], 'dim_in': [ 25,35,48 ] }
                ])

    
def show():
    result = col.find()
    print("All TV Model Profiles:")
    for document in result:
        print(document)

def query_one(): #returns models whose tags = ["family", "formal"] in this order
    query = {'tags' : {'$eq': ["family", "formal"] } }
    a = col.find(query)
    for doc in a:
        print(doc)
    print("-------------------------------")
    query2 = {'tags' : ["family", "formal"] }
    b = col.find(query2)
    for doc in b:
        print(doc)
    print("-------------------------------")
    
def query_two_a(): #returns models whose tags = ["family", "formal"] or ["formal", "family"]
    query2 = { '$or' : [ {'tags':  ["family", "formal"]}, {'tags':  ["formal", "family"]}]}
    b = col.find(query2)
    for doc in b:
        print(doc)
    print("-------------------------------")

def query_two_b():#returns models whose as long as "family" and "formal" both appear in 'tags', regardless of order
    query = { 'tags'   : { '$all': ["family", "formal"] } } 
    a = col.find(query)
    for doc in a:
        print(doc)
    print("-------------------------------")
def query_three(): #returns models who has "family" in tags
    query = { 'tags' : "family" } 
    a = col.find(query)
    for doc in a:
        print(doc)
    print("-------------------------------")
    query2 = {'tags' : {'$in':  ["family"] } }
    b = col.find(query2)
    for doc in b:
        print(doc)
    print("-------------------------------")
#-----main program-----
#models is the database, and TvModels is the collection in models
import pymongo
client = pymongo.MongoClient("127.0.0.1", 27017)
client.drop_database
db = client.get_database("models")
collections = db.collection_names()

if 'TvModels' in collections:
    dropCollections()
    
print("Existing collection(s):", collections)
col = db.get_collection("TvModels")
insertModels()


client.close()
