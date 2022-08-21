import sqlite3
DATABASE = 'register.db'

def createTable():
    print(DATABASE)
    conn = sqlite3.connect(DATABASE)
    conn.execute("PRAGMA foreign_keys = on")
    file = open("TASK4_1ClementNg_ver2.sql", 'r')
    sqlFile = file.read()
    file.close()

    sqlCommands =sqlFile.split(';')
    for command in sqlCommands:
        conn.execute(command)
    conn.commit()
    conn.close()
    
    
    #print(sqlCommands)
def menu(): #get input from user
    inputList = [] #[studID, venue, session, activity, performance/race/contact, cost]
    stuID = input("Please enter 6-digit Student ID:")
    inputList.append(stuID)
    venue = input("Enter venue of activity:")
    inputList.append(venue)
    session = input("Enter the session (ie. AM or PM):")
    inputList.append(session)
    activity = input("Enter type of activity (ie. A, C, S):")
    inputList.append(activity)
    if activity == 'A':
        performance = input("Enter: 'True'- performance arts and 'False'- Visual Arts")
        inputList.append(performance)
    if activity == 'C':
        race = input("Enter your race:")
        inputList.append(race)
    if activity == 'S':
        contact = input("Enter: 'C'-Contact Sports and 'NC'-Non-contact Sports")
        inputList.append(contact)
        cost = input("Enter cost of the activity:") #should not be more than $50
        inputList.append(cost)
    return inputList

def Task4_3():
    conn = sqlite3.connect(DATABASE)
    userSession = input("Enter the session (ie. AM or PM):")
    cursor = conn.execute("SELECT * FROM Registration WHERE Session = ?", (userSession,))
    print("------------------------------------------")
    print("{0:^12}|{1:^7}|{2:^10}|{3:^10}|".format("Student ID","Type","Venue","Session")) #Header
    print("------------------------------------------")
    for row in cursor:
        print("{0:^12}|{1:^7}|{2:^10}|{3:^10}|".format(row[0],row[1],row[2],row[3]))
    conn.close()
    
def insertToTableValues(data): ##[studID, venue, session, activity, performance/race/contact, cost]
    conn = sqlite3.connect(DATABASE)
    # Insert into Registration Table
    reg_type = data[3]

    conn.execute('INSERT INTO Registration(StudentID, Type, Venue, Session) VALUES(?,?,?,?)',
                 (data[0], reg_type, data[1], data[2]))

    # Insert into specific tables
    if reg_type == 'A':
        
        conn.execute('INSERT INTO Arts(ID, Performance) VALUES(?,?)',
                     (data[0], data[4]))
    elif reg_type == 'C':
       
        conn.execute('INSERT INTO Cultural(ID, Race) VALUES(?,?)',
                     (data[0], data[4]))
    elif reg_type == 'S':
        
        conn.execute('INSERT INTO Sports(ID, Contact, Cost) VALUES(?,?, ?)',
                     (data[0], data[4], data[5]))
    conn.commit()
    conn.close()
#------------
#main program
#------------
createTable()
conn = sqlite3.connect(DATABASE)
while True:
    inputUser = menu()
    insertToTableValues(inputUser)
    option = input("Do you wish register another activity? (Y/N):")
    if option =="N":
        break
conn.close()
