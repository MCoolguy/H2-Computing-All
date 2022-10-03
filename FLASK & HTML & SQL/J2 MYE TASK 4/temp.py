import sqlite3
results = []
conn = sqlite3.connect("equipment.db")
cursor = conn.execute("SELECT SerialNumber,Type FROM Device WHERE Location =?",("Office 51"))

row = cursor.fetchall()