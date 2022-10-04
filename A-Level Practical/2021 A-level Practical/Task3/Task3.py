class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        

    

class LinkedList:
    def __init__(self):
        self.head = None #Node object
        
    def insert(self, integer_value):
        node = Node(integer_value)
        node.next = self.head
        self.head = node        
    
    def delete(self, integer_value):
        if self.head == None:
            return None
        
        curr = self.head
        prev = None
        found = False
        
        while curr.next != None:
            if curr.data == integer_value:
                found = True
                break
                
            prev = curr
            curr = curr.next
        
        if curr.data == integer_value or found == True:
            if curr == self.head:
                self.head = curr.next
            else:
                prev.next = curr.next
        else:
            return None
            
    def search(self, integer_value):
        if self.head == None:
            return False
        
        curr = self.head
        prev = None
        found = False
        
        while curr.next != None:
            if curr.data == integer_value:
                return True
                
            prev = curr
            curr = curr.next
        
        if curr.data == integer_value:
                return True
        else:
            return False       
        
    def count(self):
        if self.head == None:
            return 0
        
        curr = self.head
        count = 1
        
        while curr.next != None:              
            prev = curr
            curr = curr.next
            count += 1
            
        return count
        
    def to_String(self):
        if self.head == None:
            return "[]"
        curr = self.head
        lst = []
        
        while curr.next != None:
            lst.append(curr.data)
            curr = curr.next
        
        lst.append(curr.data)
        
        return str(lst)
    
    

LL = LinkedList()
file = open("Task3data.txt","r")
for line in file:
    LL.insert(int(line.strip()))
    
    
#print(LL.head.next.next.next.next.next.next.next.next.next.next)    
#print(LL.delete(0))
#print(LL.to_String())

class SortedLinkedList(LinkedList):
    def __init__(self):
        super().__init__()

    def insert(self, integer_value):
        node = Node(integer_value)
        
        if self.head == None:
            self.head = node
        else:
            curr = self.head
            prev = None
        
            while curr != None:
                if curr.data > integer_value:
                    break
                prev = curr
                curr = curr.next
                
            if curr == self.head:
                node.next = curr
                self.head = node
            else:
                prev.next = node
                node.next = curr
                
                
class Queue(LinkedList):
    def __init__(self):
        super().__init__()
    def enqueue(self, integer_value):
        node = Node(integer_value)
        
        if self.head == None:            
            self.head = node  
        else:
            curr = self.head
       
            while curr.next != None:
                curr = curr.next
                
            curr.next = node
            
    def dequeue(self):
        if self.head == None:
            return None
        else:
            temp = self.head
            self.head = self.head.next
            return temp.data