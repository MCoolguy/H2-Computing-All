class Node:
    def __init__(self,data,nextnode=None):
        self.data = data
        self.nextnode = nextnode


class LinkedList:
    def __init__(self,head,tail):
        self.head = None
        self.tail = None
        self.size = 0
        
    def length(self):
        return self.size()
    
    def isEmpty(self):
        return self.size == 0
    
    def enequeue(self,data):
        node = Node(data)
        if self.isEmpty():
            self.head = node
        else:
            self.tail.nextnode = node
        
        self.tail = node
        self.size += 1
        
    def dequeue(self):
        dequeuedNode = self.head.data
        self.head = self.head.nextnode
        self.size -=1
        if self.isEmpty():
            self.tail = None
        return dequeuedNode
            
            
class Queue:
    def __init__(self,Data,Front,Rear):
        self.Data =[None for i in range(21)]
        self.Front = 0
        self.Rear = 0 
    
    def IsEmpty(self):
        return self.Rear == 0
    
    def IsFull(self):
        return self.Rear == len(self.Data) - 1
    
    def enQueue(self,item):
        if self.IsFull() == False:
            if self.IsEmpty():
                self.Front +=1
                
            self.Rear +=1
            self.Data[self.Rear] = item
        
    
    def deQueue(self,item):
        if self.Front == self.Rear:
            self.Front, self.Rear = 0,0
        else:
            firstitem = self.Data[self.Front]
            self.Front +=1
        return firstitem
    
    def Peek(self):
        return self.Data[self.Front]
    
    def Size(self):
        return len(self.Data[self.Front:self.Rear]) + 1
    
    def Display(self):
        print(self.Data[self.Front:self.Rear+1])
            
            