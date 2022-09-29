import sqlite3 

conn  = sqlite3.connect("students.db")
cursor = conn.cursor()
cursor.execute("SELECT count(*) FROM Student WHERE Student.Gender ='F'")

averageMweight = cursor.fetchone()[0]


print(averageMweight)
    
