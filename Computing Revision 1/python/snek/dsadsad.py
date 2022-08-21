class Queue:
    
    def __init__(self,size): 
        self.QueueArray = [None] * (size+1) 
        self.Head = 0
        self.Tail = 1
        
    
    def IsEmpty(self):
        if self.Head == 0:
            return True
        else:
            return False
        
    def IsFull(self): 
        if self.Tail == len(self.QueueArray):
            return True
        else: 
            return False
        
    def enqueue(self, item): 
        if self.IsFull() == False:  
            if self.IsEmpty() == True: 
                self.Head += 1
            self.Tail += 1 
            self.QueueArray[self.Tail-1] = item
            

        
    def dequeue(self): 
        first_q_element = self.QueueArray[self.Head] 
        if self.Head == self.Tail: 
            self.Head, self.Tail = 0,1 
        else:
            self.Head -= 1 
        return(first_q_element)


#DO NOT DELETE OR MODIFY THE FOLLOWING CODE
#==========================================
q = Queue(3) 
a = (len(q.QueueArray) == 4)
print(q.Tail)
b = (q.Tail == 1)
h = (q.Head == 0)
q.enqueue("Mac")
q.enqueue("Ben")
q.enqueue("Dog")
q.enqueue("Can")

print(q.QueueArray)
print(q.Head)
print(q.QueueArray[q.Head])
c = (q.QueueArray[q.Head] == "Mac")
print(q.Tail)
d = (q.Tail == 4)
e = (q.dequeue() == "Mac")
f = (q.QueueArray[q.Head] == "Ben")
q.dequeue()
q.dequeue()
q.dequeue()
 

