class Page:
    def __init__(self):
        self.page_address = ""
        self.page_title = ""
        self.time_stamp = ""
        
    def get_address(self):
        return self.page_address
    
    def get_title(self):
        return self.page_title
    
    def get_date(self):
        return self.time_stamp[0:10]
    
    def get_hour(self):
        return self.time_stamp[10:-1]
    
    def display(self):
        return ("Page("+self.page_address+','+self.page_title+','+self.timestamp+')')
    
class 
        