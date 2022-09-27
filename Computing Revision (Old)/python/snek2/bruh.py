class ConnectionNode:
    def __init__(self):
        self.data = ""
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def isListEmpty(self):
        if self.head ==None:
            return True

    def listLength(self):
        return self.head

    def insertEnd(self,item):
            if ConnectionNode.next == 11: 
            return
            
        ConnectionNode.data[ConnectionNode.next] = item
        
        if self.head == -1:
            self.ead = 0
            self.NextFree += 1
            return
        
        self.Nodes[self.NextFree-1].UpdateNext(self.NextFree) 
        self.NextFree += 1
        

    def insertHead(self,pos):

    def deleteAt(self,pos):

    def deleteEnd(self,item):

    def printList(self):



