import pymongo


client = pymongo.MongoClient("127.0.0.1",27017)
databases  = client.database_names()
db = client.get_database("Models")
col = db.get_collection("tvModels")





client.close()