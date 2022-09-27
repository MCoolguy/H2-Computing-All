
def CreateHashTable():
        records = [["",""]for i in range(500)]
        return records
    
    
def StoreData(hta):
    myFile = open("HASHEDDATA.TXT","r")
    for rec in myFile:
        rec = rec.strip()
        rec1 = rec.split(",")
        
        index = rec1[0]
        name = rec1[1]
        tel = rec1[2]
        
        people = [name,tel]
        hta[int(index)] = people
        
    myFile.close()
    
    return hta


def GenerateHash(searchname):
    hashtotal =0
    position = 0
    for char in searchname:
        ascii = ord(char)
        position +=1
        temp = ascii * position
        hashtotal += temp
    return hashtotal %500


def Search(SearchName):
    hash_key = GenerateHash(SearchName)
    if SearchName == hashtable[hash_key][0]: #if searchname is found at location of hashed searchname, return index, name and telephone number
        return (hash_key, hashtable[hash_key][0], hashtable[hash_key][1])
    else:
        if SearchName != hashtable[hash_key][0]:
            while True:
                hash_key += 1 #loop increment hash key until searchname is found/not found at all
                if SearchName == hashtable[hash_key][0]: #if searchname is found at location of hashed searchname, return index, name and telephone number
                    return (hash_key, hashtable[hash_key][0], hashtable[hash_key][1])
                if hashtable[hash_key][0] == "":
                    return "NOT FOUND"
        
#DO NOT EDIT OR DELETE THE FOLLOWING CODE
#========================================
hashtable = CreateHashTable()