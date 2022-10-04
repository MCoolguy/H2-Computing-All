class DataStructure:
    def __init__(self):
        self.LL = []
        self.head = -1
        self.tail = -1
    
    def display(self):
        print(self.LL[self.head:self.tail])
        
        
class Node:
    def __init__(self):
        self.data = ""
        self.nextpointer = -1
        
    def getdata(self):
        return self.data
    
    def getnextpointer(self):
        return self.nextpointer
    
    def setdata(self,value):
        self.data = value
        
    def setnextpointer(self,value):
        self.nextpointer = value
        


class Stack(DataStructure):
    def __init__(self):
        super().__init__()
        
    def insert(self,value):
        node = Node()
        node.setdata(value)
        if self.head ==-1:
            self.head =0
        
        self.LL.append(node)
        
        if self.tail !=-1:
            self.LL[self.tail].setnextpointer(self.LL.index(node))
        
        self.tail = self.LL.index(node)
        
    
    def delete(self):
        node = self.LL[self.tail]
        self.tail -=1 
        
        if self.tail ==-1: #last item
            self.head = -1
            self.LL = []
        
        return node.getdata()
    
    def display(self):
        if self.head == -1:
            print("Empty Stack")
        
        dic = dict()
        n = 0
        
        tempnode = self.LL[self.head]
        pointer = tempnode.getnextpointer()
        while pointer != -1:
            data,pointer = tempnode.getdata(),tempnode.getnextpointer()
            dic[data] = n
            n+= 1
            tempnode = self.LL[self.nextpointer]
        
    
 
 
 
    
class Queue(DataStructure):
    def __init__(self):
        super().__init__()
    
    def insert(self,value):
        node = Node()
        node.setdata(value)
        if self.head ==-1:
            self.head  = 0 
            
        self.LL.append(node)
        
        if self.tail != -1:
            self.LL[self.tail].setnextpointer(self.LL.index(node))
        
        self.tail = self.LL.index(node)
        
    def delete(self):
        node = self.LL[self.head]
        self.head = node.getnextpointer()
        if self.head ==-1:
            self.tail = -1
            self.LL = []
            
        return node.getdata()
    
