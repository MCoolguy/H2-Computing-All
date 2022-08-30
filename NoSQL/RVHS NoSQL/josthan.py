import pymongo
client = pymongo.MongoClient('127.0.0.1',27017)
db = client.get_database('supermarket')
collection_names = client.collection_names()
if 'items' in collection_names:
    db.drop_collection('items')
col = db.get_collection('items')

file = open('supermarket_items.txt','r')
file.readline()
for line in file:
    line = line.strip()
    name,item_type,price = line.split(',')
    col.insert_one({'item_name':name,'item_type':item_type,'price':price})