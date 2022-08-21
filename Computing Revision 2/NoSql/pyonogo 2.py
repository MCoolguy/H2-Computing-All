import pymongo

client = pymongo.MongoClient("127.0.0.1",27017)
olddatabases = client.database_names()
#print("they be: ", databases)
if 'Models' in olddatabases:
    client.drop_database("Models")
    newdatabases = client.database_names()
    print("The databases are: ", newdatabases)

db = client.get_database("Models")
col = db.get_collection("tvModels")



db.tvModels.insert_many ([
   { 'name': "Alice", 'age': 25, 'tags': ["outgoing", "family"], 'dim_in': [ 28,22,26 ] },
   { 'name': "Belle", 'age': 31, 'tags': ["formal", "family", "plain"], 'dim_in': [ 32,26,29 ]},
   { 'name': "Cindy", 'age': 13, 'tags': ["family", "formal"], 'dim_in': [ 19,18,17 ] },
   { 'name': "Daisy", 'age': 75, 'tags': ["healthcare", "food"], 'dim_in': [ 38,40,43 ] },
   { 'name': "Eleanor", 'age': 65, 'tags': ["food", "sports"], 'dim_in': [ 36,37,38 ] }
])

#c = db.collection_names("entertainment")
#print("Collections in entertainment database: ",c)
#print(client.list_database_names())
result = db.tvModels.find({'tags':["family","formal"]})
for doc in result:
    print("exact match:" ,doc)
result2 = db.tvModels.find({ 'tags':{'$all' : ["family","formal"]}})
for doc in result2:
    print("exists :", doc)

result3 = db.tvModels.find({ 'tags':{'$in' : ["family"]}})
for doc in result3:
    print("family exists :", doc)

result4 = db.tvModels.find({ 'dim_in':{'$gt' : 25}})
for doc in result4:
    print("dim_in larger than 25 :", doc)

result5 = db.tvModels.find({'$and':[{ 'age':{'$lte' : 35}},{ 'tags':{'$in' : ["outgoing"]}}]})
for doc in result5:
    print("age lt 35 and outgoing :", doc)

result6 = db.tvModels.find({'$or':[{ 'age':{'$lte' : 35}},{ 'tags':{'$in' : ["outgoing"]}}]})
for doc in result6:
    print("age lt 35 or outgoing :", doc)

client.close()

