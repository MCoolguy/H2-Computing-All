class SongRecord:
    def _init_(self, SongID = "", SongTitle = ""):
        self.SongID = SongID
        self.SongTitle = SongTitle
        
class HashTable:
    def __init__(self, size):
        self.Size = size
        #initialises Size attribute with value size
        #Size : integer
        self.Array = [[] for i in range(self.Size)]
        #initialises Array attribute to store size number of Python lists
        #Array : ARRAY[0:size-1] OF LIST
        
        #resolve aliasing
        
    def Hash(self, SongID):
        sum_ASCII = 0
        for character in SongID:
            sum_ASCII += ord(character)
        remainder = sum_ASCII%self.Size
        return remainder
        #sums the ASCII value of each character in SongID
        #returns the remainder when the sum is divided by the size of Array
        
    def Display(self):
        print("Song ID".ljust(10) + "Song Title".ljust(20))
        for item in self.Array:
            for record in item:
                print(record[0].ljust(10) + record[1].ljust(20))
    def Add(self, SongID, SongTitle):
        hash_key = self.Hash(SongID)
        self.Array[hash_key].append([SongID, SongTitle])#Appends SongID and SongTitle to the python list(Records) inside the array
        #instantiates a SongRecord object with SongID and SongTitle to Array
        #inserts the new object into Array
        #uses chaining to handle collisions
    def Remove(self, SongID):
        hash_key = self.Hash(SongID)
        for record in self.Array[hash_key]: #Record is the list containing SongID and SongTitle inside the list inside the Hashtable array
            if record[0] == SongID:
                self.Array[hash_key].remove(record)   
        #deletes the SongRecord with SongID from Array
        
        
    def Search(self, SongID):
        hash_key = self.Hash(SongID)
        for record in range(len(self.Array[hash_key])):
            if SongID == self.Array[hash_key][record][0]: #checks if SongID is equal to the first item in Records inside the list inside Hashtable array
                return self.Array[hash_key][record][1] #returns SongTitle which is at the 1st index of Records
        else:
            return "NONE"
        #uses hash table search to find the SongRecord with SongID in Array
        #returns the associated SongTitle if found or "NONE" if not found