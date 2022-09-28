import sqlite3

conn = sqlite3.connect("equipment.db")

monitors = []
monitorfile = open("MONITORS.txt",'r')
for line in monitorfile:
    monitors.append([line.strip()])
for count in range(len(monitors)):
    SerialNumber,Model,Location,DateOfPurchase,WrittenOff,DateCleaned = "".join(monitors[count]).split(',')
    conn.execute("INSERT INTO 'Monitor'(SerialNumber,Model,Location,DateOfPurchase,WrittenOff,DateCleaned)VALUES(?,?,?,?,?,?)",(SerialNumber,Model,Location,DateOfPurchase,WrittenOff,DateCleaned))
    conn.commit()

laptops = []
laptopfile = open("LAPTOPS.txt",'r')
for line in laptopfile:
    laptops.append([line.strip()])
for count in range(len(laptops)):
    SerialNumber,Model,Location,DateOfPurchase,WrittenOff,WeightKg = "".join(laptops[count]).split(',')
    conn.execute("INSERT INTO 'Laptop'(SerialNumber,Model,Location,DateOfPurchase,WrittenOff,WeightKg)VALUES(?,?,?,?,?,?)",(SerialNumber,Model,Location,DateOfPurchase,WrittenOff,WeightKg))
    conn.commit()
    
printers = []
printerfile = open("PRINTERS.txt",'r')
for line in printerfile:
    printers.append([line.strip()])
for count in range(len(printers)):
    SerialNumber,Model,Location,DateOfPurchase,WrittenOff,Toner,DateChanged = "".join(printers[count]).split(',')
    conn.execute("INSERT INTO 'Printer'(SerialNumber,Model,Location,DateOfPurchase,WrittenOff,Toner,DateChanged)VALUES(?,?,?,?,?,?,?)",(SerialNumber,Model,Location,DateOfPurchase,WrittenOff,Toner,DateChanged))
    conn.commit()
    

    
    
conn.close()
