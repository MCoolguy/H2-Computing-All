import datetime
import sqlite3
#from datetime import date
#Task 3.1
class Member:
    def __init__(self):
        self.memberID = ""
        self.first_name = ""
        self.surname = ""
        self.contact_number = ""
        self.last_visit = "2022-8-28"
        self.memberType = ""
        
    def showMember(self):
        return self.memberID,self.first_name,self.surname,self.contact_number,self.last_visit
          
    def isActive(self):
        todaysdate =datetime.datetime.today().date()
        difference = todaysdate - datetime.datetime(self.last_visit,"%Y-%m-%d").date()
        days = difference.days
        if days<30:
            return True
        return False
    
class NormalMember(Member):
    def __init__(self):
        super().__init__()
        self.stored_value = 0.00
    
    def showMember(self):
        return super().showMember() + (self.memberType,)


class AnnualMember(Member):
    def __init__(self):
        super().__init__()
        self.annual_fee = 0
        self.date_register = "2022-8-28"

    def showMember(self):
        return super().showMember() + (self.memberType,)
 
#Task 3.2       
file = open("members.txt",'r')
listofmembers = []
for line in file:
    memberId,first_name,sur_name,contact_number,memberType = line.strip().split(',')
    if memberType == "normal":
        member = NormalMember()
        member.memberID = memberId
        member.first_name = first_name
        member.surname = sur_name
        member.contact_number = contact_number
        member.memberType = memberType
        listofmembers.append(member)
    else:
        member = AnnualMember()
        member.memberID = memberId
        member.first_name = first_name
        member.surname = sur_name
        member.contact_number = contact_number
        member.memberType = memberType
        listofmembers.append(member)
        
    #print(member.showMember())
file.close()


#Task 3.3
connection = sqlite3.connect("JPgym.db")
#file2 = open("JPgym.sql")
# sqlFile = file2.read()
# file2.close()
# sqlcommands = sqlFile.split(';')
# for command in sqlcommands:
#     connection.execute(command)
connection.execute("DROP TABLE IF EXISTS 'Member'")
connection.execute("CREATE TABLE IF NOT EXISTS 'Member' ('MemberID' TEXT PRIMARY KEY, 'FirstName' TEXT,'Surname' TEXT, 'ContactNo' TEXT, 'LastVisit' TEXT, 'MemberType' TEXT);")
for member in listofmembers:
    connection.execute("INSERT INTO Member('MemberID','FirstName','SurName','ContactNo','LastVisit','MemberType')\
                    VALUES(?,?,?,?,?,?)",member.showMember())
    connection.commit()
    
cursor = connection.execute("SELECT FirstName,SurName,ContactNo,MemberType FROM Member "+"WHERE MemberType='normal'"+"ORDER BY FirstName")
rows = cursor.fetchall()
#print(rows)
print("First Name".ljust(20)+"Sur Name".ljust(20)+"Contact No".ljust(20))

for row in rows:
    #print(row[1])
    print(row[0].ljust(20)+row[1].ljust(20)+row[2].ljust(20))
    
connection.close()
