import sqlite3 

conn = sqlite3.connect("students.db")
cursor = conn.cursor()
studentIDs = []
cursor.execute("SELECT StudentID from StudentHealthRecord")
studentIDs = cursor.fetchall()


id = 13
print(studentIDs)
print((12,) in studentIDs)
# for count in range(len(studentIDs)):
#     if id in studentIDs[count]:
#         print("it is in")
#     else:
#         print("not in")

# print(12 in studentIDs[13])
