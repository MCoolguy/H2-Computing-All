import sqlite3

con = sqlite3.connect("JPFashion.db")


file = open("CUSTOMER.TXT","r")
file.readline()
for line in file:
    #print(line.strip())
    Email,FirstName,LastName,ContactNumber,DOB,Address =line.strip().split(',')
    con.execute("INSERT INTO Customer(Email,FirstName,LastName,ContactNumber,DOB,Address) VALUES(?,?,?,?,?,?)",(Email,FirstName,LastName,ContactNumber,DOB,Address))
    con.commit()
file.close()

file2 = open("PRODUCT.TXT","r")
file2.readline()
for line in file2:
    CatalogueNumber,Category,Brand,Size,Fee = line.strip().split(',')
    con.execute("INSERT INTO Product(CatalogueNumber,Category,Brand,Size,Fee) VALUES(?,?,?,?,?)",(CatalogueNumber,Category,Brand,Size,Fee))
    con.commit()
file2.close()


file3 = open("CUSTOMERRENTAL.TXT","r")
file3.readline()
for line in file3:
    ID,CatalogueNumber,Returned = line.strip().split(',')
    con.execute("INSERT INTO CustomerRental(ID,CatalogueNumber,Returned) VALULES(?,?,?)",(ID,CatalogueNumber,Returned))
    con.commit()
file3.close()

file4 = open("PRODUCTRENTAL.TXT","r")
file4.readline()
for line in file4:
    ID,CatalogueNumber,Returned = line.strip().split(',')
    con.execute("INSERT INTO ProductRental(ID,CatalogueNumber,Returned) VALUES(?,?,?)",(ID,CatalogueNumber,Returned))
    con.commit()
file4.close()
    


con.close()
    
        
