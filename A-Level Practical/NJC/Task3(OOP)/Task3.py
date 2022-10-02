class Page:
    def __init__(self,page_address,page_title,time_stamp):
        self.page_address = page_address
        self.page_title = page_title
        self.time_stamp = time_stamp
        
    def get_address(self):
        return self.page_address
    
    def get_title(self):
        return self.page_title
    
    def get_date(self):
        return self.time_stamp[0:10]
    
    def get_hour(self):
        return self.time_stamp[10:-1]
    
    def display(self):
        return ("Page("+self.page_address+', '+self.page_title+', '+self.time_stamp+')')
    
class Stack:
    def __init__(self):
        self.array = []
        self.tail = -1
        
    def push(self,page_object):
        self.array.append(page_object)
        self.tail +=1 
        
    def pop(self):
        if self.tail == -1:
            return None
        
        object = self.array[self.tail]
        self.tail -=1
        return object
    
    def count(self):
        if self.tail ==-1:
            return 0 
        
        return self.tail +1
    
    def search(self,page_title):
        for item in self.array:
            if item.get_title() == page_title:
                return True
        return False
    
    def to_String(self):
        items = []
        for index in range(self.tail+1):
            items.append(self.array[index].display())
        print('['+", ".join(items)+']')
        
        
file = open("TASK3DATA1.csv","r")
file.readline()
stack = Stack()
for line in file:
    id,page_address,page_title,time_stamp = line.strip().split(',')
    page = Page(page_address,page_title,time_stamp)  
    stack.push(page)
    
    
#print(stack.count())
#stack.to_String()
file.close()       
       
class ModStack(Stack):
    def __init__(self):
        super().__init__()
        self.array=[""for count in range(12)]
        
    def push(self,page_object):
        self.tail +=1 
        if self.tail ==len(self.array):
            for index in range(len(self.array)-1):
                self.array[index] = self.array[index +1]
                self.tail = len(self.array)-1
        
        self.array[self.tail] = page_object
        
        
file2 = open("TASK3DATA2.csv","r")
file2.readline()
modstack = ModStack()

for line in file2:
    id,page_address,page_title,time_stamp = line.strip().split(',')
    page = Page(page_address,page_title,time_stamp)
    modstack.push(page)
    
    
#modstack.to_String()
# print(modstack.search("Object-based global firmware"))
# print(stack.search('Secured content-based data-warehouse'))
# print(stack.search('Secured content-based data-warehouse '))
file2.close()

class PageNode(Page):
    def __init__(self,page_address,page_title,time_stamp):
        super().__init__(page_address,page_title,time_stamp)
        self.next= None
        
    def get_next(self):
        return self.next
    
    def set_next(self,next):
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = -1
        self.tail = -1
        
    def insert(self,page_object):
        if self.head ==-1:
            self.head = page_object
            self.tail = page_object
        else:
            self.tail.next = page_object
            self.tail = page_object
            

            
    def delete(self,page_title):
        if self.head ==-1:
            return None
        
        if self.head.get_title()==page_title:
            temp = self.head
            self.head = self.head.next
            return temp
        
        current = self.head
        prev= self.head
        while current:
            if current.get_title() == page_title:
                prev.next = current.next
                return current 
            prev = current
            current = current.next
        return None 
    
    def to_String(self):
        if self.head ==-1:
            print("empty")
        items = []
        final = []
        cursor = self.head
        while cursor!=None:
            items.append(cursor)
            cursor = cursor.next
        for page in items:
            final.append('Page('+page.page_address+', '+page.page_title+', '+page.time_stamp+')')
        print('['+", ".join(final)+']')
        
    def visit(self,page_title):
        to_top  = self.delete(page_title)
        if to_top:
            to_top.next = None
        else:
            return "Page Not Found in History"

        self.insert(to_top)
        return
    
                

        
        
file2 = open("TASK3DATA2.csv","r")
file2.readline()
LL = LinkedList()

for line in file2:
    id,page_address,page_title,time_stamp = line.strip().split(',')
    page = PageNode(page_address,page_title,time_stamp)
    LL.insert(page)
    
# print(LL.delete("Function-based asynchronous product"))
# print(LL.delete("Face to face bottom-line core"))

print(LL.visit('Streamlined didactic matrix'))
print(LL.visit('Open-source zero tolerance installation'))

LL.to_String()

            

        
        
            
    


    
    
            
            
            

        
    

    

        
        
        
        