class Node():
    def __init__(self, data = ""):
        self.data = data
        self.leftPtr = -1
        self.rightPtr = -1

    def setData(self, s):
        self.data = s

    def setLeftPtr(self, x):
        self.leftPtr = x

    def setRightPtr(self, y):
        self.rightPtr = y

    def getData(self):
        return self.data

    def getLeftPtr(self):
        return self.leftPtr

    def getRightPtr(self):
        return self.rightPtr


class Tree():
    def __init__(self, size = 10):
        self.tree = [None for count in range(size)]
        self.root = -1
        self.NextFree = 0

    def add(self,newItem):
        if self.root == -1:#empty tree
            self.tree[0] = Node(newItem)
            self.root = 0
            self.NextFree += 1
            return
        temp_node = self.tree[self.root]
        self.add_helper(temp_node, newItem)
        return


    def add_helper(self,temp_node, newItem):
        data = temp_node.getData()
        if data > newItem and self.tree[temp_node.getLeftPtr()] == None:
            self.tree[self.NextFree] = Node(newItem)
            temp_node.setLeftPtr(self.NextFree)
            self.NextFree += 1
            return
        
        if data < newItem and self.tree[temp_node.getRightPtr()] == None:
            self.tree[self.NextFree] = Node(newItem)
            temp_node.setRightPtr(self.NextFree)
            self.NextFree += 1
            return
        if data > newItem:
            return self.add_helper(self.tree[temp_node.getLeftPtr()], newItem)
        if data < newItem:
            return self.add_helper(self.tree[temp_node.getRightPtr()], newItem)


    def print(self):
        print("{0:10}{1:10}{2:10}".format("data","leftPtr","rightPtr"))
        for item in self.tree:
            if item != None:
                print("{0:10}{1:10}{2:10}".format(item.getData(),str(item.getLeftPtr()), str(item.getRightPtr()) ) )


    def inOrderTraversal(self):
        node = self.tree[self.root]
        print("In order traversal:")
        return self.inOrderHelper(node)
    
    def inOrderHelper(self, node):
        #L-P_R
        if node == None:
            return
        self.inOrderHelper(self.tree[node.getLeftPtr()] )
        print(node.getData())
        self.inOrderHelper(self.tree[node.getRightPtr()] )
        return
def task3_2():
    tree = Tree()
    tree.add("Dave")
    tree.add("Fred")
    tree.add("Ed")
    tree.add("Greg")
    tree.add("Bob")
    tree.add("Cid")
    tree.add("Ali")
    tree.print()
    return tree

if __name__ == "__main__":
    tree = task3_2()
    print()
    tree.inOrderTraversal()
    
    
    
