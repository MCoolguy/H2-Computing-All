import datetime

def numofdays(date1, date2):
    return (date2-date1).days

#x = str(datetime.date.today())
#year,month,day = x.split('-')

date1 = datetime.date.today()
#date2 = datetime.date(2019, 2, 25)




class Member:
    def __init__(self,memberID,first_name,surname,contact_number,last_visit,memberType=None):
        self.memberID = memberID
        self.first_name = first_name
        self.surname = surname
        self.contact_number = contact_number
        self.last_visit = last_visit
        self.memberType = memberType
        
        
    def showMember(self):
        print(self.memberType,self.first_name,self.surname,self.contact_number,self.last_visit)
        
    def isActive(self):
        date2 = datetime.date(self.last_visit)
        diff = numofdays(date1,date2)
        if diff<=30:
            return True
        return False
    
class NormalMember(Member):
    def __init__(self,stored_value):
        super().__init__(NormalMember)
        self.stored_value = stored_value
    
    def showMember(self):
        return super().showMember()
        
        
        
        
        
        
m = Member('20221234','Bob','John','88339262','321312321')
m.showMember()