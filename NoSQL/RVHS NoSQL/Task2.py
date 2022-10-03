import pymongo

client = pymongo.MongoClient("127.0.0.1", 27017)
if "supermarket" in client.list_database_names():
    client.drop_database('supermarket')
db = client["supermarket"]
if "items" in db.list_collection_names():
        db.drop_collection("items")
coll = db["items"]
#print(db.list_collection_names())
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
#results = coll.find()
#for doc in results:
#    print(doc)
while True:
    print("Choose an option\n1. Find cost by item name.\n2. Find items by type.\n3. Update cost by item name.\n4.Quit")
    choice =input("Choose an option: ")
    if choice =="4":
        print("Program quitted")
        break
    elif choice =="1":
        itemname = input("Type an item name: ")
        result = coll.find({'item_name':itemname})
        for doc in result:
            print(itemname +" each cost $" +doc['price'])
    elif choice =="2":
        itemtype = input("Type an item type: ")
        results = coll.find({'item_type':itemtype})
        count = 0
        for doc in results:
            count += 1
            print(str(count)+" "+str(doc['item_name']))
    
    elif choice =="3":
        updateitem = input("Type an item name you want to update price: ")
        updateprice = input("Type a new update price: ")
        search = {'item_name':updateitem}
        update = {'$set':{'price':updateprice}}
        coll.update_many(search, update)
        
        

client.close()