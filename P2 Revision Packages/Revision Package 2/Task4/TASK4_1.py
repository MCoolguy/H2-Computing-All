import sqlite3

def CreateTable():
    connection = sqlite3.connect("EntryDB.db")
    file = open("TASK4_1.sql",'r')
    sqlfile = file.read()
    file.close()
    #print(sql)
    sqlcommands = sqlfile.split(';') #commands are split by ';'
    #print(sqlcommands)
    for command in sqlcommands:
        #print(command)
        connection.execute(command) 
    
    connection.close()
    
def importdata():
    file = open("LOCATIONS.csv","r")
    file.readline()
    locationslist = []
    for line in file:
        LocationID,Name,Address,URL = line.strip().split(',')
        locationslist.append((LocationID,Name,Address,URL))
    connection = sqlite3.connect("EntryDB.db")
    for item in locationslist:
        print(item)
        connection.execute("INSERT INTO Location('LocationID','Name','Address','URL')\
            VALUES(?,?,?,?)",item)
        connection.execute("COMMIT")
        connection.commit()
    connection.close()
    
    file.close()
    
    
CreateTable()
importdata()