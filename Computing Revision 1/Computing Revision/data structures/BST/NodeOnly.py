class BSTNode:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val
        
def insert(self, val):
    if not self.val:
        self.val = val
        return

    if self.val == val:
        return

    if val < self.val:
        if self.left:
            self.left.insert(val)
            return
        self.left = BSTNode(val)
        return

    if self.right:
        self.right.insert(val)
        return
    self.right = BSTNode(val)
    
def get_min(self):
    current = self
    while current.left is not None:
        current = current.left
    return current.val

def get_max(self):
    current = self
    while current.right is not None:
        current = current.right
    return current.val

def exists(self, val):
    if val == self.val:
        return True

    if val < self.val:
        if self.left == None:
            return False
        return self.left.exists(val)

    if self.right == None:
        return False
    return self.right.exists(val)

def inorder(self, vals):
    if self.left is not None:
        self.left.inorder(vals)
    if self.val is not None:
        vals.append(self.val)
    if self.right is not None:
        self.right.inorder(vals)
    return vals

def preorder(self, vals):
    if self.val is not None:
        vals.append(self.val)
    if self.left is not None:
        self.left.preorder(vals)
    if self.right is not None:
        self.right.preorder(vals)
    return vals

def postorder(self, vals):
    if self.left is not None:
        self.left.postorder(vals)
    if self.right is not None:
        self.right.postorder(vals)
    if self.val is not None:
        vals.append(self.val)
    return vals