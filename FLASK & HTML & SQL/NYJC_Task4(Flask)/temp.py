import sqlite3 

conn = sqlite3.connect("Task4.db")
cursor = conn.cursor()
cursor.execute("SELECT Name, Date, Time FROM Person INNER JOIN Record ON Person.id = Record.visitorId WHERE Time > '0730' AND Type = 'entry' AND Role = 'Student' ORDER BY Date ASC, Time ASC;")

data = cursor.fetchall()


print(data)