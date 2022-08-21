class Node:
    def __init__(self,data):
        self.data = data
        self.left = None 
        self.right = None
        
class Tree:
    def __init__(self):
        self.root = None
    
    def insert(self,value):
        if self.root == None:
            self.root = Node(value)
        else:
            self.inserthelp(value,self.root)
            
    def inserthelp(self,data,cur_node):
        if data<cur_node.data:
            if cur_node.left ==None:
                cur_node.left = Node(data)
            else:
                self.inserthelp(data,cur_node.left)
            
        elif data>cur_node.data:
            if cur_node.right==None:
                cur_node.right = Node(data)
            else:
                self.inserthelp(data,cur_node.right)
        else:
            print("no dupes fam")
            
    def find(self,data):
        if self.root:
            result = self.findhelp(data,self.root)
            if result==True:
                return True
            else:
                return False
        return "they aint shit here"  
      
    def findhelp(self,data,cur_node):
        if data == cur_node.data:
            return True
        elif data<cur_node.data and cur_node.left!=None:
            if cur_node.left.data== data:
                return True
            else:
                self.findhelp(data,cur_node.left)
        elif data>cur_node.data and cur_node.right!=None:
            if cur_node.right.data == data:
                return True
            else:
                self.findhelp(data,cur_node.right)
        return False     
    
    def preorder_print(self, start, traversal):
        """Root->Left->Right"""
        if start:
            traversal += (str(start.data) + "-")
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal

    def inorder_print(self, start, traversal):
        """Left->Root->Right"""
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal += (str(start.data) + "-")
            traversal = self.inorder_print(start.right, traversal)
        return traversal

    def postorder_print(self, start, traversal):
        """Left->Right->Root"""
        if start:
            traversal = self.postorder_print(start.left, traversal)
            traversal = self.postorder_print(start.right, traversal)
            traversal += (str(start.data) + "-")
        return traversal
        




        
#inorder is lefttree -> root -> righttree
#preorder is root -> lefttree -> righttree
#postorder is lefttree -> righttree -> root

bst = Tree()
bst.insert(10)
bst.insert(2)
bst.insert(1)
bst.insert(11)
bst.insert(20)
#print(bst.root.left.left.data)
#print(bst.find(120))
print(bst.inorder_print(bst.root,""))
print(bst.postorder_print(bst.root,""))
print(bst.preorder_print(bst.root,""))