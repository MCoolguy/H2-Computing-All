#Program 6 - update.py
def display():
    result = col.find()
    print("All documents in movies collection:")
    for document in result:
        print(document)

def dropCollections():
    db.drop_collection("movies")
    
def insert_doc():
    col.insert_one({"_id":1, "title":"Johnny Maths", "genre":"comedy1"}) 
    col.insert_one({"title":"Star Walls", "genre":"science fiction"})
    col.insert_one({"title":"Detection"}) #no genre
    list_to_add = []
    list_to_add.append({"title":"Badman", "genre":"adventure1", "year":2015})  #
    list_to_add.append({"title":"Averages", "genre":["science fiction","adventure1"], "year":2017}) #
    list_to_add.append({"title":"Octopus Man", "genre":"adventure1", "year":2017}) #
    list_to_add.append({"title":"Fantastic Bees", "genre":"adventure1", "year":2018}) #
    list_to_add.append({"title":"Underground", "genre":"horror", "year":2014}) #

    list_to_add.append({"title":"A", "genre":['adventure'], "year":2014}) #
    list_to_add.append({"title":"B", "genre":['adventure', 'comedy', 'horror'], "year":2014}) #
    list_to_add.append({"title":"C", "genre":"adventure", "year":2014}) #
    list_to_add.append({"title":"D", "genre":['comedy', 'adventure'], "year":2014}) #
    list_to_add.append({"title":"E", "genre":['adventure', 'comedy'], "year":2014}) #
    list_to_add.append({"title":"F", "genre":[['adventure', 'comedy'], 'apple'], "year":2014})
    col.insert_many(list_to_add)
    print("Insertion complete!")
#-----main program-----
import pymongo
client = pymongo.MongoClient("127.0.0.1", 27017)
db = client.get_database("entertainment")
collections = db.collection_names()
if 'movies' in collections:
    dropCollections()
print("Existing collection(s):", collections)
col = db.get_collection("movies")
insert_doc()
display()
#updates the value 2015 to the 'year' field of the first returned doc that satisfies the search filter
search = {'year':{'$gt':2016}}
update = {'$set':{'year':2015}} #$set can assign value into a field
col.update_one(search, update) #title "Averages" will have 'year' : 2015

#col.update_many(search, update)#'titles': "Octopus Man", "Fantastic Bees" will have 'year':2015


##search = { 'year' : { '$eq' : 2018 } }
##update = { '$unset' : { 'year' : 0 } } #$unset will remove the field 'year' from the doc entirely
##col.update_many(search, update)

#update doc that do not have the field 'year' to have 'year': 2019
##search = { 'year' : { '$exists' : False } } #look for doc that do not have the field 'year'
##update = { '$set' : { 'year' : 2019 } } #$set can assign both field and value into a doc
##col.update_many(search, update)


#return values of fields 'title', 'genre' and 'year' of a
#doc that has 'title': 'Fantastic Bees' and 'genre' : 'adventure'


query = { '$and': [ {'title' : { '$eq' : 'Fantastic Bees' }},
                    {'genre' : { '$eq' : 'adventure'}}
                    ]
          }
projection = {'title' : 1, 'genre' : 1, 'year' : 1, '_id' : 0}
result = col.find(query, projection)
for i in result:
    print(i)



#-----------------delete---------------
# .delete_one(query) --> removes the one entire document that fulfils query
# .delete_many(query) --> removes all documents that fulfil query

#delete all documents that have 'genre': 'adventure' OR if they have 'year' less than 2015
##query = {'$or' : [ { 'genre' : { '$eq' : 'adventure'} },
##                   { 'year': { '$lt' : 2015 }}
##                   ]
##         }
##
##col.delete_many(query)






client.close()
