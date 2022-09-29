import sqlite3

conn = sqlite3.connect("equipment.db")
cursor = conn.execute("SELECT Device.SerialNumber,Device.Type FROM DEVICE WHERE Device.Location =?",("Office 51",))

row = cursor.fetchall()
serialnumbers = []
types = []
for count in range(len(row)):
    serialnumbers.append(row[count][0])
    types.append(row[count][1])
    
    
print(serialnumbers)
print(types)