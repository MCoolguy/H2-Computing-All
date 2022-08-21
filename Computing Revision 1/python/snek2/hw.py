class Node:
    def __init__(self,data,nextnode=None):
        self.data = data
        self.nextnode = nextnode


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        
    def length(self):
        return self.size()
    
    def isEmpty(self):
        return self.size == 0
    
    def add(self,data):
        node = Node(data)
        if self.isEmpty():
            self.head = node
        else:
            self.tail.nextnode = node
        
        self.tail = node
        self.size += 1
        
    def delete(self):
        dequeuedNode = self.head.data
        self.head = self.head.nextnode
        self.size -=1
        if self.isEmpty():
            self.tail = None
        return dequeuedNode
    
L = LinkedList()
L.add(1)
L.add(43)
L.add(21)
print(L.head.data)