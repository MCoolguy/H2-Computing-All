class Tree:    
    def __init__(self): #Constructor 
        self.tree = [Node("")] * 32    #array of seven Node objects from index 0
        for i in range(32):
                self.tree[i] = Node("") #avoids aliasing   (i.e: pointing to same object)
        self.root = 0 # NULL value
        self.nextfree = -1
      
         
           
    def add(self, newItem):
        self.tree[self.nextfree].setData(newItem) 
        if self.root == 0:
            self.root = self.nextfree
        else:
            self.readd(self.tree[self.root],newItem)
        self.nextfree +=1
          
    def readd(self,node,item):
        if item<node.getData():
            if node.getLeftPtr() != 0:
                self.readd(self.tree[node.getLeftPtr()],item)
            else:
                node.leftPtr = self.nextfree
        else:
            if node.getRightPtr() != 0:
                self.readd(self.tree[node.getRightPtr()],item)
            else:
                node.setRightPtr(self.nextfree)
# Print the tree
    def print(self):
      if self.left:
         self.left.print()
      print( self.data),
      if self.right:
         self.right.print()
        
    
        
class Node:
    def __init__(self, data): #Constructor
           self.data = data #String data type
           self.leftPtr = 0 #NULL value
           self.rightPtr = 0
           
    def setData(self,s):
        self.data = s
    def setLeftPtr(self,x):
        self.leftPtr = x
    def setRightPtr(self,y):
        self.rightPtr = y
    def getData(self):
        return self.data
    def getLeftPtr(self):
        return self.leftPtr
    def getRightPtr(self):
        return self.rightPtr