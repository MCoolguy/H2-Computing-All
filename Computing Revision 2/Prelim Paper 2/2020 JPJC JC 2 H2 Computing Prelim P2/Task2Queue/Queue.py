class Queue:
    def __init__(self):
        self.Items = [""for i in range(5)]
        self.Front = -1
        self.Rear = -1
        
    def isEmpty(self):
        return self.Front ==-1
    
    def isFull(self):
        if self.Rear == len(self.Items)-1:
            return True
        return False
    
    def Enqueue(self,string):
        if self.isFull() == False:
            if self.IsEmpty():
                self.Front+=1
                
            self.Rear += 1    
            self.Items[self.Rear] = string

    def deQueue(self):
        if self.Front == self.Rear:
            self.Front,self.Rear = -1,-1
        else:
            firstQelement = self.Data[self.Front]
            self.Front +=1 
        return firstQelement
    
    
class CircularQueue(Queue):
    def __init__(self):
        super().__init__()
    
    def isFull(self):
        if (self.Rear+1)%len(self.Items)==self.Front:
            return True
        return False  
    
    def Enqueue(self,string):
        if self.isFull() == False:
            if super().isEmpty():
                self.Front+=1
                self.Rear +=1
                self.Items[self.Rear] = string
        else:       
            self.Rear = (self.Rear+1)%len(self.Items)    
            self.Items[self.Rear] = string

    def deQueue(self):
        if self.Front == self.Rear:
            temp = self.Items[self.Front]
            self.Front,self.Rear = -1,-1
            return temp 
        else:
            temp = self.Data[self.Front]
            self.Front = (self.Front+1)%len(self.Items)
        return temp  
    
    def printCQueue(self):
            if(self.Front == -1):
                print("No element in the circular queue")

            elif (self.Rear >= self.Front):
                for i in range(self.Front, self.Rear + 1):
                    print(self.Items[i], end=" ")
                print()
            else:
                for i in range(self.Front, len(self.Items)):
                    print(self.Items[i], end=" ")
                for i in range(0, self.Rear + 1):
                    print(self.Items[i], end=" ")
                print()
                
                
obj = CircularQueue()
obj.Enqueue('1')
obj.Enqueue('2')
obj.Enqueue('3')
obj.Enqueue('4')
obj.Enqueue('5')
print("Initial queue")
obj.printCQueue()

obj.deQueue()
print("After removing an element from the queue")
obj.printCQueue()