import pymongo, json

def database_exist():
    global client
    client = pymongo.MongoClient("127.0.0.1", 27017)
    if "jp_mobile" in client.list_database_names():
        print("\nREMOVED 'jp_mobile' FROM DATABASE RECORDS")
        client.drop_database("jp_mobile")
    return

def user_input_interface():
    brand = input("brand: ")
    model = input("model: ")
    colour = input("colour: ")
    price = int(input("price: "))
    quantity = int(input("quantity: "))
    gifts = []
    while True:
        data = input("gifts (input one at a time, input 0 if no more gifts): ")
        if data == '0':
            break
        gifts.append(data)
        
    dic = {}
    dic["brand"], dic["model"], dic["colour"], dic["price"], dic["quantity"]= brand, model, colour, price, quantity
    if gifts != []:
        dic["free gift (s)"] = gifts
    return dic

def load_collection():
    global client
    client = pymongo.MongoClient("127.0.0.1", 27017)
    db = client.get_database("jp_mobile")
    coll = db.get_collection("phone")
    return coll

def task_4_1():   
    file = open("items.JSON", 'r')
    with file as data:
        load = json.load(data)
    print("\nLOADED JSON FILE\n")
    file.close()
    database_exist()
    coll = load_collection()
    coll.insert_many(load)
    client.close()
    print("\nEXECUTED 4.1\n")

def task_4_2():
    data = user_input_interface() #data is a dictionary type
    coll = load_collection()
    #assuming that brand and model are composite key such that it is unique
    #when we perform .find(), we should only return one result for each brand and model
    query = {"brand": {'$eq' : data["brand"] }, 
             "model": {'$eq' : data['model'] } , 
             "colour" : {'$eq' : data["colour"] } 
            } 
    cur = coll.find(query)
    
    print(data, '\n')
    
    cur = list(cur)
    if len(cur) == 0:
        coll.insert_one(data)
        print("\nINSERTED\n")
    else:
        row = cur[0]
        quantity = row["quantity"] + data["quantity"]
        coll.update_one(query, {"$set": {"quantity": quantity, "price": data["price"] } } )
        print("\nUPDATED\n")
        
    client.close()
    print("\nEXECUTED 4.2\n")


def display_all():
    coll = load_collection()
    cur = coll.find({}, {'_id': 0} ) 
    print()
    
    print("{0:15}{1:15}{2:15}{3:15}{4:15}{5:15}".format("brand   |", "model   |", "colour   |", "price   |", "quantity   |", "free gift(s)"))
    for row in cur:
        gift = "None"
        if "free gift (s)" in row:
            gift = row["free gift (s)"]
        
        print("{0:15}{1:15}{2:15}{3:15}{4:15}{5:15}".format(row["brand"], row["model"] ,row["colour"], 
                                                            str(row["price"]), str(row["quantity"]), str(gift))
             )
    print()

def task_4_3():
    display_all()

def main():
    task_4_1()
    #run 4.2 twice to insert 2 documents
    display_all()
    for count in range(2):
        task_4_2()
    task_4_3()
    
if __name__ == "__main__":
    main()
