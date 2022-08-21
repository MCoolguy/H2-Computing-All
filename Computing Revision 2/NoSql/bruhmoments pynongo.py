import pymongo

client = pymongo.MongoClient("127.0.0.1",27017)
databases = client.database_names()
print("they be: ", databases)

db = client.get_database("bruh_moments")
coll = db.get_collection("moments")
coll.insert_one({"_id":1, 'title':"finger","genre":"comedy"})

c = db.collection_names("bruh_moments")
print("Collections in entertainment database: ",c)




client.close()

