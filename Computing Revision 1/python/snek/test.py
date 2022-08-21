
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
         
    def getHeight(self):
        if self.root ==0:
            return 0
        queue = [self.tree[self.root]]
        height = -1
        while queue !=[]:
            node_counter = len(queue)
            while node_counter != 0:
                node = queue.pop()
                node_counter -= 1
                if self.tree[node.getLeftPtr()].getData() != "":
                    queue.append(self.tree[node.getLeftPtr()])
                if self.tree[node.getRightPtr()].getData() != "":
                    queue.append(self.tree[node.getRightPtr()])
            height += 1
        return height
        
    
        

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
    



t = Tree()

t.add("Cat")
t.add("Ant")
t.add("Dog")
t.add("Bat")

a = t.getHeight() == 2

print(a)