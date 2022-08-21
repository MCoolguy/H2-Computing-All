import sqlite3



staff = open("STAFF.TXT",'r')
school = open("SCHOOL.TXT",'r')


#Objective: To create staff and school lists consisting of tuple objects containing the information of each staff and schools respectively
staff_lst = []
school_lst = []

staff.readline()
school.readline()

for line in staff:
    code, name, department, contact = line.strip().split(',')
    staff_lst.append( (code, name, department, contact) )

for line in school:
    code, name, address = line.strip().split(',')
    school_lst.append( (code, name, address) )


staff.close()
school.close()


#carry out sql statements first
sql_statements = open("TASK1_1_21S23_CHIAMENGJIT.sql" , 'r')

conn = sqlite3.connect("schools.db")

full_statement = ''
for line in sql_statements:
    full_statement += line

statement = full_statement.split(';\n')

for item in statement:
    conn.execute(item)

conn.commit()


#insertion of items from the text file into the database
for item in school_lst:
    conn.execute("INSERT INTO schools ('SchoolCode','Name','Address')\
                VALUES(?,?,?)", item)

    conn.execute("COMMIT")
    conn.commit()

for item in staff_lst:
    conn.execute("INSERT INTO staff ('SchoolCode','Name','Department', 'Contact')\
                VALUES(?,?,?,?)", item)

    conn.execute("COMMIT")
    conn.commit()


conn.close()
