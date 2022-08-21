class SongRecord:
    def __init__(self,SongID ="",SongTitle=""):
        self.SongID = ""
        self.SongTitle =""

class HashTable:
    def __init__(self, size):
        #initialises Size attribute with value size
        #Size : integer
        self.Size = size
        #initialises Array attribute to store size number of Python lists
        #Array : ARRAY[0:size-1] OF LIST
        self.Array = [[]for i in range (self.Size-1)]
        #resolve aliasing
        
        
    def Hash(self, SongID):
        #sums the ASCII value of each character in SongID
        ascii = 0
        temp = 0
        for char in SongID:
            ascii = ord(char)
            temp += ascii
        return temp%(self.Size)
            
        #returns the remainder when the sum is divided by the size of Array
        

    def Display(self):
        #displays the content of Array neatly
        print(self.SongID).center(4)+self.SongTitle.center(28)
        

    def Add(self, SongID, SongTitle):
        #instantiates a SongRecord object with SongID and SongTitle to Array
        song = SongRecord()
        #inserts the new object into Array
        self.Array.append(song)
        #uses chaining to handle collisions


    def Remove(self, SongID):
        #deletes the SongRecord with SongID from Array
        
        
    def Search(self, SongID):
        #uses hash table search to find the SongRecord with SongID in Array
        #returns the associated SongTitle if found or "NONE" if not found
        
        if records[hashindex][0] =="":
            return "NOT FOUND"
        if records[hashindex][0] != "" and records[hashindex][0] == searchname:
            temp = hashindex
            while True:
                hashindex = (hashindex+1)%500
                print(hashindex)
                #if records[hashindex][0] == searchname:
                # return hashindex,records[hashindex][0],records[hashindex][1]
                if hashindex == temp:
                    return "NOT FOUND"

        if records[hashindex][0] == searchname:
            return hashindex,records[hashindex][0],records[hashindex][1]
        
        
        
#DO NOT EDIT OR DELETE THE FOLLOWING CODE
#========================================
hta1 = HashTable(13) #hash table of size 13
hta1.Add("EL0078","Hotel California")
hta1.Add("CL0123","K-King")
hta1.Add("CL0010","Red Bean")
hta1.Add("EL7810","Lady in Red")
hta1.Add("CL2310","Ninja")
hta1.Add("EL1610","Tears in Heaven")
hta1.Add("CL3210","Beach")
hta1.Add("EL0611","Unchained Melody")

hta1.Remove("CL2310")
hta1.Remove("EL0078")
hta1.Add("EL0870","Witulah")

a = hta1.Search("CL3210")
b = hta1.Search("CL2310")
c = hta1.Search("EL1610")
d = hta1.Search("EL0611")
e = hta1.Search("EL0870")
        
