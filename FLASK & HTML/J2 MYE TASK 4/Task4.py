import sqlite3
#TASK 4.2
class School:
    def __init__(self):
        self.id = 0
        self.name = ""
        self.zone = ""
        
    def safe_name():
        return ""
    
    def as_record():
        return ('','')
    
class PrimarySchool(School):
    def __init__(self):
        super().__init__()
        self.level = "primary"
        self.YearsOfStudy = 6
    
    def as_record(self):
        return super().as_record() + (self.level,self.YearsOfStudy)
    
class SecondarySchool(School):
    def __init__(self):
        super().__init__()
        self.level = "secondary"
        self.YearsOfStudy = 4
    
    def as_record(self):
        return super().as_record() + (self.level,self.YearsOfStudy)

class JuniorCollege(School):
    def __init__(self):
        super().__init__()
        self.level = "junior college"
        self.YearsOfStudy = 2
    
    def as_record(self):
        return super().as_record() + (self.level,self.YearsOfStudy)
    
#Task 4.3 + 4.4
file = open("school_info.csv","r")
primaryschools = []
secondaryschools = []
jcs = []
con = sqlite3.connect("schools.db")

for line in file:
    school_id,school_name,zone,level = line.strip().split(',')
    if level == "PRIMARY":
        school = PrimarySchool()
        school.id = school_id
        school.name = school_name
        school.zone = zone
        primaryschools.append(school)
        
        con.execute("INSERT INTO 'School'('SchoolID','Name','Zone','Level','YearsOfStudy')\
                    VALUES(?,?,?,?,?)",(school.id,school.name,school.zone,school.level,school.YearsOfStudy))
        con.commit()
        
    elif level == "SECONDARY":
        school = SecondarySchool()
        school.id = school_id
        school.name = school_name
        school.zone = zone
        secondaryschools.append(school)
        con.execute("INSERT INTO 'School'('SchoolID','Name','Zone','Level','YearsOfStudy')\
                    VALUES(?,?,?,?,?)",(school.id,school.name,school.zone,school.level,school.YearsOfStudy))
        con.commit()
    elif level == 'JUNIOR COLLEGE':
        school = JuniorCollege()
        school.id = school_id
        school.name = school_name
        school.zone = zone
        jcs.append(school)
        con.execute("INSERT INTO 'School'('SchoolID','Name','Zone','Level','YearsOfStudy')\
                    VALUES(?,?,?,?,?)",(school.id,school.name,school.zone,school.level,school.YearsOfStudy))
        con.commit()

file2 = open("subjects_offered.csv","r")
file2.readline()
for line in file2:
    school_id,subject_desc = line.strip().split(',')
    con.execute("INSERT INTO 'Subject'('SchoolID','SubjectName')\
        VALUES(?,?)", (school_id,subject_desc))
    con.commit()


con.close()
file.close()
file2.close()
    
    
        