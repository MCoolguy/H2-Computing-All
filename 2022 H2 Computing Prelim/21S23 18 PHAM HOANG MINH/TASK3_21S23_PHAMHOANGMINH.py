import pymongo,json
from datetime import date
#Task 3.2
client = pymongo.MongoClient("127.0.0.1",27017)
db = client.get_database("StyleTheory")
if 'Rental' in db.collection_names(): #If collection already exists we drop it and create a new one
    db.drop_collection('Rental')
coll = db.get_collection('Rental') 

file = open("RENTAL.json","r")
data = json.load(file)
coll.insert_many(data)


#results = coll.find()
#for doc in results:
#    print(doc)

while True:
    print("Style Theory\nOption 1 - Insert new rental\nOption 2 - Update existing rental\nOption 3 - Quit")
    choice = input("Enter your option (1, 2, or 3): ")
    if choice =="3":
        break

    elif choice =="1":
        catalogueNumber = input("enter the catalogue number: ")
        brand = input("enter the brand: ")
        category = input("enter the category: ")
        DailyRentalFee = input("Enter the daily rental fee: ")
        if category =="Apparel":
            size = input("Enter the size: ")
        email = input("Enter your email: ")
        startDate = input("Enter the start date: ")
        endDate = input("Enter the end date: ")
        if category =="Apparel":
            coll.insert_one({'catalogueNumber':catalogueNumber,'brand':brand,'category':category,'rental':DailyRentalFee,'size':size,'email':email,'startDate':startDate,'endDate':endDate})
        else:
            coll.insert_one({'catalogueNumber':catalogueNumber,'brand':brand,'category':category,'rental':DailyRentalFee,'email':email,'startDate':startDate,'endDate':endDate})

    elif choice =="2":
        catalogueNumber = int(input("enter the catalogue number: "))
        startDate = input("Enter the start date: ")
        endDate = input("Enter the end date: ")
        search = {'catalogueNumber':catalogueNumber}
        query = {'$set':{'endDate':endDate}}
        coll.update_one(search,query)
        
#Task 3.3
def daydifference(start,end): #Function to calculate the difference in number of days between two dates
    year,month,day = start.split('-')
    f_date = date(int(year),int(month),int(day))
    year1,month1,day1 = end.split('-')
    l_date = date(int(year1),int(month1),int(day1))
    delta = l_date - f_date
    return delta.days
        
def display_all():
    print("catalogue number".ljust(20)+"brand".ljust(10)+"category".ljust(20)+"rental".ljust(10)+"size".ljust(10)+"customer's email".ljust(30)+"start date".ljust(20)+"end date".ljust(20)+"rental fee".ljust(20))
    results = coll.find()
    for doc in results:
        startdate = doc['startDate']
        enddate = doc['endDate']
        rentalfee = doc['rental']
        diff = daydifference(startdate,enddate) #Calculates the differences in days
        amount = diff*rentalfee
        if 'size' not in doc:
            print(str(doc["catalogueNumber"]).ljust(20)+doc["brand"].ljust(10)+doc["category"].ljust(20)+str(doc["rental"]).ljust(10)+"NA".ljust(10)+doc["email"].ljust(30)+doc["startDate"].ljust(20)+doc["endDate"].ljust(20)+str(amount).ljust(20))
        else:
            print(str(doc["catalogueNumber"]).ljust(20)+doc["brand"].ljust(10)+doc["category"].ljust(20)+str(doc["rental"]).ljust(10)+str(doc["size"]).ljust(10)+doc["email"].ljust(30)+doc["startDate"].ljust(20)+doc["endDate"].ljust(20)+str(amount).ljust(20))

display_all()




client.close() ##closes client
