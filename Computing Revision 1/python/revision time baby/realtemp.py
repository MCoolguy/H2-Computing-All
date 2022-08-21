class Customer :
    def __init__(self,Name,Priority):
        self.Name = Name
        self.Priority = Priority
        
class PriorityQueue:
    def __init__(self):
        self.Data = [Customer("",-1) for i in range(20)]
        self.Front = -1
        self.Rear = -1
    
    def IsEmpty(self):
        return self.Front == -1
        
    def IsFull(self):
        return self.Rear == len(self.Data) -1

    def enQueue(self, name,prio):
        customer = Customer(name,prio)
        #print(customer.Name,customer.Priority)
        if self.IsEmpty():
            self.Front +=1 
            self.Data.insert(0,customer) 
            return
        else:
            for x in range(0, len(self.Data)-1):
                print("x value is" ,x)
                print("prio is: " ,self.Data[x].Priority)
                print(test.Data[x].Name)
                if customer.Priority > self.Data[x].Priority:
                        self.Data.insert(x,customer)
                        return
                elif customer.Priority == self.Data[x].Priority:
                    self.Data.insert(x+1, customer)
                    #print(self.Data[x].Name)
                    self.Rear +=1
                    return
                elif customer.Priority < self.Data[x].Priority:
                    pass
        #print(self.Data[0].Name)

    def deQueue(self):
        #print(self.Data[0].Name)
        return self.Data.pop(0).Name



    
#DO NOT EDIT OR DELETE THE FOLLOWING CODE
#========================================
test = PriorityQueue()
test.enQueue("Anne",2)
test.enQueue("Bobby",0)
#print(test.Data[0].Name)
#print(test.Data[2].Name)

#test.enQueue("Cash",2)
#test.enQueue("Davian",1)
#print(test.Data[4].Name)

a = test.deQueue()
b = test.deQueue()
c = test.deQueue()
d = test.deQueue()

#print(a,b,c,d)

    
    
