import sqlite3
results = []
conn = sqlite3.connect("equipment.db")
cursor = conn.execute("SELECT Device.SerialNumber,Device.Type FROM Device WHERE Device.Location =?",('Office 51',))

row = cursor.fetchall()
print(len(row))