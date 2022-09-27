class Node:
    def __init__(self):
        self.Data = ""
        self.LeftPtr = Node()
        self.RightPtr = Node()


class Tree:
    def __init__(self):
        Root = Node()
        
    def AddNode(self,data):
        if self.Root.getData() =="":
            self.Root.setData(data)
            return
        
        prev = None
        cur = self.Root
        
        while cur != None:
            prev = cur
            if data < cur.getData():
                cur = cur.getLeft()
            else:
                cur = cur.getRight()
        
        newnode = Node()
        newnode.setData(data)
        if data<prev.getData():
            prev.setLeft(newnode)
        else:
            prev.setright(newnode)
            
    def SearchNode(self,key):
        if self.Root is None or self.Root.Data == key:
            return self.Root
    
        # Key is greater than root's key
        if self.Root.Data < key:
            return SearchNode(self.Root.RightPtr,key)
    
        # Key is smaller than root's key
        return SearchNode(self.Root.LeftPtr,key)
    
    def Traversal(self):
        stack = []
        cur = self.Root
        while True:
            if cur != None:
                stack.append(cur)
                cur = cur.LeftPtr
            elif stack != []:
                cur = stack.pop()
                stack.append(cur.Data)
                cur = cur.RightPtr
            else:
                break
        return 