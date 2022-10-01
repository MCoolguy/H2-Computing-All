import datetime


class LibraryItem:
    def __init__(self):
        self.item_id = ""
        self.title = ""
        self.loaned_by = ""
        self.due_date = ""
        
    def is_on_loan(self):
        if self.loaned_by =="":
            return False
        return True
    
    def return_item(self):
        self.loaned_by = ""
        
    def loan_to(self,user_id):
        if self.loaned_by =="":
            self.loaned_by = user_id
            return True
        return False
    
    def print_details(self):
        print("Title: " + self.title)
        if self.loaned_by =="":
            print("Loaned by: No one")
        else:
            print("Loaned by: " + self.loaned_by)  
        print("Due date : " + self.due_date) 
        
        
class Book(LibraryItem):
    def __init__(self):
        super().__init__()
        self.author = ""
        self.category =""
        self.reserved_by = ""

    def is_reserved(self):
        if self.reserved_by =="":
            return False
        return True
    
    def release(self):
        self.reserved_by = ""
        
    def reserve_for(self,user_id):
        if self.reserved_by =="":
            self.reserved_by = user_id
            return True
        return False
        
    def print_details(self):
        super().print_details()
        print("Author: " + self.author)
        print("Category: " +self.category)
        if self.reserved_by =="":
            print("Reserved by: No one")
        else:
            print("Reserved by: " + self.reserved_by) 
        print() 

class CompactDisc(LibraryItem):
    def __init__(self):
        super().__init__()
        self.artist = ""
        self.genre = ""
        
    def print_details(self):
        super().print_details()
        print("Genre: " + self.genre)
        print("Artist: " +self.artist)
        print()
            
#task 2.3
file = open("libraryitems.txt")
libraryitems= []

for line in file:
    line = line.strip()
    if line[0]=='B':
        item_id,title,author,category = line.split(',')
        book=Book()
        book.item_id = item_id
        book.title = title
        book.author = author
        book.category = category
        libraryitems.append(book)
        book.print_details()
        print()
        
    elif line[0] =='C':
        item_id,title,artist,genre = line.split(',')
        cd=CompactDisc()
        cd.item_id = item_id
        cd.title = title
        cd.artist = artist
        cd.genre = genre
        libraryitems.append(cd)
        cd.print_details()
        print()
        


#Main Task 2.4
user_id = "S1111111H"
user_id2 = "S1222222D"

today = datetime.date.today()
# add 1 week to today's date
reservedate = today + datetime.timedelta(weeks=1)
# convert date object to string
loandate = today.strftime('%d-%m-%Y')
reservedate = reservedate.strftime('%d-%m-%Y')

print(libraryitems)
for object in libraryitems:
    object.loaned_by  = user_id
    object.due_date = reservedate
    if type(object)==type(Book()):
        object.reservedby = user_id2
    
    object.print_details()




             

 