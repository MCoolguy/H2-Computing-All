class Node:
    def __init__(self):
        self.data = ""
        self.left = None
        self.right = None
    
    def set_data(self,data):
        self.data = data
        
    def get_data(self):
        return self.data
        
    def set_left(self,node):
        self.left = node
    
    def get_left(self):
        return self.left

    def set_right(self,node):
        self.right = node
    
    def get_right(self):
        return self.right
    
    
class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def set_root(self,node):
        self.root = node
        
    def get_root(self):
        return self.root
    
    def addNode(self,node):
        if self.root == None:
            newnode = Node()
            newnode.set_data(node)
            self.root = newnode
        else:
            self.addNodehelper(node,self.root)
            
            

    def addNodehelper(self,node,currentnode):
        if node<currentnode.get_data():
            if currentnode.get_left() ==None:
                    newnode = Node()
                    newnode.set_data(node)
                    currentnode.set_left(newnode)
            else:
                self.addNodehelper(node,currentnode.left)
        elif node>currentnode.get_data():
            if currentnode.get_right() ==None:
                    newnode = Node()
                    newnode.set_data(node)
                    currentnode.set_right(newnode)
            else:
                self.addNodehelper(node,currentnode.right)
        
            
        
    def inOrderTraversal(self):
        if self.root == None:
            return("empty BST")
        else:
            inorderlist = self.inOrderTraversalhelper(self.root,[])
        return inorderlist
        
    def inOrderTraversalhelper(self,rootnode,list):
        if rootnode:
            list=self.inOrderTraversalhelper(rootnode.left,list)
            list.append(rootnode.get_data())
            list=self.inOrderTraversalhelper(rootnode.right,list)
        return list
       
        
        
        
    
        
bst = BinarySearchTree()
bst.addNode("mango")
bst.addNode("pineapple")
bst.addNode("banana")
bst.addNode("cucumber")

a = (bst.get_root().data == "mango")
b = (bst.get_root().left.data == "banana")
c = (bst.get_root().right.data == "pineapple")
lst = bst.inOrderTraversal()

#print(a,b,c)
print(lst)