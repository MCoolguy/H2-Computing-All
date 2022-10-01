def hashfunction(key):
    address = int(key)%31
    return address

#print(hashfunction(666))
hashtable =  [None for count in range(31)]

def add():
    file = open("IDs.txt","r")
    for line in file:
        membershipID, name = line.strip().split(',')
        address = hashfunction(membershipID)
        if hashtable[address]!=None:
            address = (2**int(membershipID)) %31
            
        hashtable[address] = name,membershipID
        
        
def display():
    records = []
    for item in hashtable:
        if item!=None:
            records.append({item,hashtable.index(item)})
    print(records)
    
    
def search(membershipNo):
    for data in hashtable:
        if hashtable[membershipNo]==data:
            print(data)
            return
    print("Not here")
    return
        
        
    
add()
display()
search(13)
search(2)
search(15)
search(19)
search(20)

    
        