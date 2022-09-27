Max = 20
hashtable = [None for i in range(Max)]

file = open("KEYS2.TXT","r")
for line in file:
    IDnumber = int(line.strip())
    Address = IDnumber % Max
    if hashtable[Address] == "":
        hashtable[Address] = IDnumber
    else:
        while hashtable[Address]!=None:
            if Address == Max-1:
                Address = 0
            else:
                Address += 1
        hashtable[Address] = IDnumber
            
#print(hashtable)
def search():
    searchid = input("What ID do you want to find: ")
    for count in range(Max):
        if hashtable[count] == int(searchid):
            return count
    return "it aint here"

print(search())
print(hashtable)