import sqlite3
DATABASE = 'schools.db'

file1 = open("SCHOOL.TXT",'r')
file2 = open("STAFF.TXT",'r')

conn = sqlite3.connect(DATABASE)
#insertion into school
header = file1.readline()
file1read = file1.read().split('\n')
#print(file1read)

data1 = []
listsize = 0
for data in file1read:
    listsize += 1
    data = data.split(',')
    data1.extend(data)
#print("data1:",data1)


counter = 0
for i in range(listsize):
    #print(data1[0+counter],data1[1+counter],data1[2+counter])
    conn.execute("INSERT INTO School(SchoolCode,Name,Address) VALUES(?,?,?)",(int(data1[0+counter]),data1[1+counter],data1[2+counter]))
    counter += 3

#insertion into staff
header = file2.readline()
file2read = file2.read().split('\n')

data2 = []
listsize = 0
for data in file2read:
    listsize += 1
    data  = data.split(',')
    data2.extend(data)

counter = 0
for i in range(listsize):
    conn.execute("INSERT INTO Staff(SchoolCode,Name,Department,Contact) VALUES(?,?,?,?)",(int(data2[0+counter]),data2[1+counter],data2[2+counter],data2[3+counter]))
    counter += 4
    
conn.commit()
conn.close()

file1.close()
file2.close()
