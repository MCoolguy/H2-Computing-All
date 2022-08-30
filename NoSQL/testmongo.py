import pymongo


client = pymongo.MongoClient("mongodb+srv://mcoolguy:minhmoc123@mongoforjpjc.nsdccjd.mongodb.net/?retryWrites=true&w=majority")
#databases  = client.database_names()
db = client.get_database("Models")
col = db.get_collection("tvModels")


#print(databases)


client.close()



#mongodb+srv://mcoolguy:minhmoc123@mongoforjpjc.nsdccjd.mongodb.net/?retryWrites=true&w=majority