import pymongo

client = pymongo.MongoClient("127.0.0.1", 27017)
db = client["supermarket"]
coll = db["items"]

file = open("supermarket_items.txt",'r')
file.readline()
itemlist = []
for line in file:
    item_name, item_type, price = line.strip().split(',')
    #print(item_name)
    itemlist.append([item_name,item_type,price])
    coll.insert_one({'item_name':item_name,'item_type':item_type,'price':price})
file.close()

#coll.insert_many({itemlist})
print(coll.find({}))
client.close()