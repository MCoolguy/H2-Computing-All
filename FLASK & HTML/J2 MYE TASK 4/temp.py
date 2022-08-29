import sqlite3
results = []
schoolname = "OUTRAM SECONDARY SCHOOL"
con = sqlite3.connect("schools.db")
cursor = con.execute("SELECT School.Name,School.Zone,School.Level,School.YearsOfStudy,Subject.SubjectName FROM School,Subject \
                     WHERE School.SchoolID = Subject.SchoolID AND School.Name = ? ",(schoolname,))

row = cursor.fetchall()
for rows in row:
    print(rows)

