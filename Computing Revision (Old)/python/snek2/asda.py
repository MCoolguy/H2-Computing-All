class Queue:
    def __init__(self):
        self.list_queue = []
    
    def enqueue(self, item):
        self.list_queue.append(item)
    
    def dequeue(self):
        self.list_queue.pop()
    
    def is_empty(self):
        return len(self.list_queue) == 0
        
    def size(self):
        return len(self.list_queue)
        
def who_wins(m,players):
    counter = 0
    if len(players)==0:
        return None
    q = Queue()
    for p in players:
        q.enqueue(p)
    counter = m
    
    while q.size()>(m-1):
        if counter ==0:
            q.dequeue()
            counter = m
        else:
            q.enqueue(q.dequeue())
            counter -=1
    return q.list_queue()

print(who_wins(2, ['poo', 'ste', 'sim', 'nic', 'luo', 'ibr', 'sie', 'zhu']))