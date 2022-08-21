class Queue:
    def __init__(self):
        self.Data = [""]*20 
        self.Front = -1
        self.End = -1
    
    def IsEmpty(self): #
        if self.Front == -1:
            return True
        else:
            return False
        
    def IsFull(self): 
        if self.End == len(self.Data)-1:
            return True
        else: 
            return False
        
    def enQueue(self, item): 
        if self.IsFull() == False: 
        
            if self.IsEmpty() == True: 
                self.Front += 1
                
            self.End += 1 
            self.Data[self.End] = item 

        
    
    def deQueue(self):
        if self.Front == self.End: 
            self.Front, self.End = -1, -1
        else:
            first_q_element = self.Data[self.Front] 
            self.Front += 1 
        return(first_q_element)

#DO NOT EDIT OR DELETE THE FOLLOWING CODE
#========================================
q = Queue()
a = (len(q.Data)==20)
c = (q.IsEmpty()==True)

lst = ["a" * n for n in range(20)]

for item in lst:
    q.enQueue(item)
    
b = (q.IsFull()==True)
q.enQueue("xxx")

d = (q.deQueue()=="")
e = (q.IsFull()==True)
