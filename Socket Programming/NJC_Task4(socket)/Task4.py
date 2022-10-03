import sqlite3

conn = sqlite3.connect('tide.db')
sql_statement = '''CREATE TABLE "Tide" (
	"RecordID"	INTEGER NOT NULL,
	"Date"	TEXT NOT NULL,
	"Time"	TEXT NOT NULL,
	"isHigh"	INTEGER NOT NULL,
	"Height"	REAL NOT NULL,
	PRIMARY KEY("RecordID")
);'''

conn.execute(sql_statement)
conn.commit()

add_to_database = '''INSERT INTO Tide(RecordID,Date,Time,isHigh,Height)
                    VALUES(?,?,?,?,?)'''
                    
                    
file = open("TIDES.txt","r")
id = 0

for line in file:
    date,time,tide,height = line.strip().split('\t')
    if tide =='LOW':
        tide = 0
    else:
        tide = 1
    conn.execute(add_to_database,(id,date,time,tide,height))
    id +=1
    conn.commit()
    
    

    

