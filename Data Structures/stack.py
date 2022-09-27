class Stack():
    def __init__(self,size):
        self.Size = size
        self.Pointer = -1
        self.Array = [""]*size
        
    def isEmpty(self):
         if self.Pointer ==0:
             return True
         return False
    def isFull(self):
        if self.Pointer ==self.Size:
            return True
        return False
    def push(self,number):
        if self.isFull() ==False:
            self.Pointer +=1
            self.Array[self.Pointer]=number
    def pop(self):
        if self.Pointer ==-1:
            return None
        else:
            result = self.Array[self.Pointer]
            self.Pointer -=1
            return result
    def peek(self):
        if self.isFull()==False:
            return self.Array[self.Pointer]
        return None