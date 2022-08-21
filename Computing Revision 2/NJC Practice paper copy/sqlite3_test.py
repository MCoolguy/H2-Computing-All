import sqlite3
def search_html(school, department):
    connection = sqlite3.connect("schools.db")
    sql_statement = """
                    SELECT schools.SchoolCode, staff.Name, staff.Department, staff.Contact, schools.Address
                    FROM schools, staff
                    WHERE staff.SchoolCode = schools.SchoolCode AND schools.Name LIKE ? AND staff.Department LIKE ?
                    """

    cur = connection.cursor()
    cur.execute(sql_statement,('%'+school+'%',department))
    rows = cur.fetchall()
    for row in rows:
        print(row)



search_html("NTU High School","Arts")
        
