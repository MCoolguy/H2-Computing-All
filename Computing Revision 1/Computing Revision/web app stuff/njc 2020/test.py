##
##file = open("SCHOOL.txt" , 'r')
##file.readline()
##listofschools = []
##for line in file:
##    line = line.strip()
##    listofschools.append(line)
##print(listofschools)

import sqlite3

connection = sqlite3.connect("schools.db")
cursor = connection.execute("SELECT SchoolCode,Name,Address FROM school")
cursor2 = connection.execute("SELECT SchoolCode,Department,Name,Contact FROM staff")
rows = cursor.fetchall()
rows2 = cursor2.fetchall()

listofstaff = []
listofschools = []
for row in rows:
    listofschools.append(row)
for row in rows2:
    listofstaff.append(row)

print(listofschools)
print(listofstaff)
