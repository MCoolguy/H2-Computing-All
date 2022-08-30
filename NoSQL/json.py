import pymongo
import json

client=pymongo.MongoClient("127.0.0.1",27017)
with open('input.json') as file :
    data = json.load(file)
client['entertainment']['movies'].insert_many(data)
client.close()
