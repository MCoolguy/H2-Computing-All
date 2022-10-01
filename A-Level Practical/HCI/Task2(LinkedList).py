class Node:
    def __init__(self,data,next):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
        
    def insert(self,word,p):
        if p==1 or self.size==0: #Empty linked list so add at front
            self.head = Node(word,self.head)    
        
        else:
            if p>self.size: 
                p  = self.size +1
            
            cursor = self.head
            for i in range(1,p-1):
                cursor = cursor.next  #find the correct index
                
            cursor.next = Node(word,cursor.next)
            
        self.size +=1  
                
    def delete(self,p):
        if p==1 or self.size==1:#only one in linked list
            self.head = self.head.next
        
        else:
            if p>self.size:
                p = self.size
            
            cursor  = self.head
            for i in range(1,p-1):
                cursor=cursor.next
            cursor.next = cursor.next.next
        
        self.size -=1
        
    def search(self,word):
        cursor = self.head
        for count in range(self.size):
            if cursor.data ==word:
                return True
            cursor = cursor.next

        return False
    
    def to_String(self):
        items = []
        cursor = self.head
        while cursor !=None:
            items.append(cursor.data)
            cursor = cursor.next
        
        print(" ".join(items))
        
        
LL =  LinkedList()

LL.insert('1st element',1) 
LL.insert('last element',4) 
LL.insert('2nd element',2) 
LL.insert('3rd element',3) 
LL.delete(4)
LL.delete(1)
#LL.to_String()

class Stack(LinkedList):
    def __init__(self):
        super().__init__()
        
    def push(self,word):
        super().insert(word,self.size+1)
        
    def pop(self):
        super().delete(self.size+1)
        
        
class Queue(LinkedList):
    def __init__(self):
        super().__init__()
        
    def enqueue(self,word):
        super().insert(word,self.size+1)
        
    def dequeue(self):
        super().delete(1)
        
        
        
stack = Stack()
stack.push('apple')
stack.push('pear')
stack.push('carrot')
stack.pop()
stack.to_String()


q = Queue()
q.enqueue('apple')
q.enqueue('pear')
q.enqueue('carrot')
q.dequeue()
q.to_String()

      


        
                
        
                
            
                
        
        
    