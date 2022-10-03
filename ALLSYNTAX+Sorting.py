#SORTING
def bubblesort(lst):
    for i in range(len(lst)-1):
        for j in range(len(lst)-1):
            if lst[j] > lst[j+1]:
                lst[j],lst[j+1] = lst[j+1],lst[j]
                
    return lst


def insertionsort(lst):
    for i in range(1,len(lst)):
        key = lst[i]
        j = i-1
        while j>=0 and key<lst[j]:
            lst[j+1] = lst[j]
            j-=1
        lst[j+1] = key
    return lst    
        
        

def merge(left,right):
    finallist = []
    while len(left)!=0 and len(right)!=0:
        if left[0]<right[0]:
            finallist.append(left[0])
            left.pop(0)
        else:
            finallist.append(right[0])
            right.pop(0)
            
    while len(left)!=0:
            finallist.append(left[0])
            left.pop(0)
            
    while len(right)!=0:
        finallist.append(right[0])
        right.pop(0)
        
    return finallist

def mergesort(lst):
    n = len(lst)
    if n==1:
        return lst
    
    left = lst[:n//2]
    right = lst[n//2:]
    
    left = mergesort(left)
    right = mergesort(right)
    
    return merge(left,right)
            

def partition(lst,low,high):
    i = low
    pivot = lst[high]
    for j in range(low,high):
        if lst[j]<=pivot:
            lst[j],lst[i] = lst[i],lst[j]
            i +=1
    lst[high],lst[i] = lst[i],lst[high]
    
    return i 

def quicksort(lst,low,high):
    if low<high:
        partition_index = partition(lst,low,high)
        quicksort(lst,low,partition_index-1)
        quicksort(lst,partition_index+1,high)
        
    return lst 

testlist = [7,5,6,9,3,2,1,1,1,3,2,4,5,9,99,12,0,4,8,-2,0]
#print(bubblesort(testlist))
#print(insertionsort(testlist))
#print(mergesort(testlist))
#print(quicksort(testlist,0,len(testlist)-1))


#FLASK

from flask import *
app = Flask(__name__,template_folder = 'templatefoldername')
@app.route('/')
def home():
    name = "Bobby"
    return render_template('home.html',name=name)
@app.route('/submissionform', methods = ['POST'])
def form():
    return render_template('form.html')
if __name__ =='__main__':
    app.run(port=1234)


###SQL

import sqlite3
conn = sqlite3.connect('databasename.db')
conn.execute('INSERT INTO Table(Name,Gender,Age)VALUES(?,?,?)',('Bobby','Male',18))
conn.commit()
conn.close()


###NOSQL

import pymongo 
client = pymongo.MongoClient('127.0.0.1',27017)
if 'database_name' in client.get_database_names(): #Check if database exists already
    client.drop_database('database_name')
db = client['database_names']  #Create new database

if 'collection_name' in db.list_collection_names(): 
    db.drop_collection('collection_name') #Not necessary if dropped database earlier
coll = db['collection_name']  #Create new collection

item_name,item_type,item_price = 'Bananas','Fruit','9.2'
coll.insert_one({'item_name':item_name,'item_type':item_type})
coll.insert_many([{item_name:"Bananas",item_type:'Fruit',item_price:'9.2'},
                  {item_name:"Apple",item_type:'Fruit',item_price:'4.5'}])
                         
                         
item_name = input("Type an item name: ")     
result = coll.find({'item_name':item_name})            
for doc in result:
    print(item_name +" each cost $" +doc['price'])

    
updateitem = input("Type an item name you want to update price: ")
updateprice = input("Type a new update price: ")
search = {'item_name':updateitem}
update = {'$set':{'price':updateprice}}
coll.update_many(search, update)    

client.close()


import socket #SERVER

listen_socket = socket.socket()
listen_socket.bind(("127.0.0.1",6789))
listen_socket.listen()

server_socket , address = listen_socket.accept()

message = "LLOLL"
server_socket.sendall(message.encode())
choice = server_socket.recv(1024).decode()

server_socket.close()   
####################
import socket #CLIENT

client_socket = socket.socket()
client_socket.connect(('127.0.0.1',6789))

message = client_socket.recv(1024)
choice = input("Enter choice: ")
client_socket.sendall(choice.encode())

client_socket.close()



