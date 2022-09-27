class Node:
    def __init__(self):
        self.Data = ""
        self.Next = None
    
    def GetData(self):
        return self.Data

    def UpdateData(self,newData):
        self.Data = newData

    def GetNext(self):
        return self.Next

    def UpdateNext(self,newNext):
        self.Next = newNext


    
class LinkedList:
    def __init__(self):
            self.Nodes = [Node() for n in range(0,11)] 
            self.Head = -1 
            self.NextFree = 0
            
    def Add(self, item):
        if self.NextFree == 11: 
            return
            
        self.Nodes[self.NextFree].UpdateData(item)
        
        if self.Head == -1:
            self.Head = 0
            self.NextFree += 1
            return
        
        self.Nodes[self.NextFree-1].UpdateNext(self.NextFree) 
        self.NextFree += 1
        

    def Delete(self, item):
        
        if self.Nodes[self.NextFree-1] == item:
            self.NextFree -= 1
            self.Nodes[self.MextFree-1].UpdateNext(None)
            return
        
        if self.Nodes[self.Head].GetData() == item:
            self.Head = self.Nodes[self.Head].GetNext()
            return
        
        next_index = self.Nodes[self.Head].GetNext()
        current_index = self.Head
        while next_index != None:
            if self.Nodes[next_index].GetData() != item: 
                current_index = next_index
                next_index = self.Nodes[current_index].GetNext()
            else:
                break
        if next_index != None:    
            self.Nodes[current_index].UpdateNext(self.Nodes[next_index].GetNext())
        else:
            print("There is no '" + item + "' in the linked list")
            
    def Display(self):
        
        next_index = self.Head
        
        if self.Head != -1:
            while True:
                
                if next_index == None:
                    break
                print(self.Nodes[next_index].GetData())
                next_index = self.Nodes[next_index].GetNext()
                


