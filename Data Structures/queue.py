class LinearQueue1:
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
    
    
class LinearQueue2:
    
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
    

class PythonListQueue:
    def __init__(self):
        self.list_queue = []
    def isEmpty(self):
        return self.items == []
    def enqueue(self, item):
        self.list_queue.insert(0,item)
    def dequeue(self):
        return self.list_queue.pop()
    def size(self):
        return len(self.list_queue)
    

class CircularQueue:
    def __init__(self):
        self.list_queue = []
    def enqueue(self, item):
        self.list_queue.append(item)
    def dequeue(self):
        if self.size() != 0:
            item = self.list_queue[0]
            del self.list_queue[0]
            return item
        else:
            return None
        
    def size(self):
        return len(self.list_queue)