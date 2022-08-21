class Tree:
    def __init__(self):
        self.Root = Node()
        
    def AddNode(self, NewData):
        #if root node has an empty value
        if self.Root.getData() == "":
            self.Root.setData(NewData)
            return
        
        prev_node = None
        curr_node = self.Root
        
        while curr_node != None:
            prev_node = curr_node
            if NewData < curr_node.getData():
                curr_node = curr_node.getLeft()
            else:
                curr_node = curr_node.getRight()
                
        newNode = Node()
        newNode.setData(NewData)
        if NewData < prev_node.getData():
            prev_node.setLeft(newNode)
        else:
            prev_node.setRight(newNode)
        
    def SearchNode(self, Key):
        
        curr_node = self.Root
        
        while curr_node != None:
            if curr_node.getData() == Key:
                return True
            
            if Key < curr_node.getData():
                curr_node = curr_node.getLeft()
            else:
                curr_node = curr_node.getRight()
        
        return False
        
    def Traversal(self):
        #IOT is LPR
        stack = []
        current = self.Root
        while True:
            if current != None:
                stack.append(current)
                current = current.getLeft()
            elif stack != []:
                current = stack.pop()
                lst.append(current.getData())
                current = current.getRight()
            else:
                break
        return 
                
        
class Node:
    def __init__(self):
        self.Data = ""
        self.LeftPtr = None
        self.RightPtr = None
        
    def getData(self):
        return self.Data
        
    def getLeft(self):
        return self.LeftPtr
        
    def getRight(self):
        return self.RightPtr
        
    def setData(self, data):
        self.Data = data
        
    def setLeft(self, left):
        self.LeftPtr = left
        
    def setRight(self, right):
        self.RightPtr = right
#DO NOT EDIT OR DELETE THE FOLLOWING CODE
#========================================
Tree1 = Tree()
Tree1.AddNode(10)
Tree1.AddNode(5)
Tree1.AddNode(7)
Tree1.AddNode(12)
Tree1.AddNode(15)
Tree1.AddNode(6)
Tree1.AddNode(25)
print()
print(Tree1.Root.Data == 10)
print(Tree1.SearchNode(5) == True)
print(Tree1.SearchNode(20) == False)
print()
Tree1.AddNode(20)
print(Tree1.SearchNode(20) == True)
print()
lst = []
Tree1.Traversal()
print(lst)