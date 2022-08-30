import pymongo
client = pymongo.MongoClient('127.0.0.1',27017)
database_names = client.database_names()
if 'supermarket' in database_names:
    client.drop_database('supermarket')
db = client.get_database('supermarket')
col = db.get_collection('items')

file = open('supermarket_items.txt','r')
file.readline()
for line in file:
    line = line.strip()
    name,item_type,price = line.split(',')
    col.insert_one({'item_name':name,'item_type':item_type,'price':price})

print('Choose an option: ')
print('1.Find cost by item name.')
print('2.Find items by type.')
print('3.Update cost by item name.')
print('4.Quit')
while True:
    option = input("Choose an option: ")
    if option == 4:
        print('Program quitted')
        break
    elif option == 1:
        item_name = input("Type an item name: ")
        result = col.find({'item_name':{'$eq':item_name}},{'price':1})
        for doc in result:
            print(doc)
    elif option == 2:
        item_type = input("Type an item  type: ")
        result = col.find({'item_type':{'$eq':item_type}},{'item_name':1})
        for doc in result:
            print(doc)
    elif option == 3:
        update_item = input("Type a item you want to update price")
        update_price = input("Type a new update price")
        search = {'item_name':{'$eq':update_item}}
        update = {'$set':{'price':update_price}}
        col.update_one(search,update)
        
        
    
        
        
    
    
