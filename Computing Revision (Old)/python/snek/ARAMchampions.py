
class Artist():
    def __init__(self, name, dob):
        self.name = name
        self.dob = dob
        
    
    def get_name(self):
        # Fill in your code here
        return self.name
        

        
    def get_dob(self):
        # Fill in your code here
        return self.dob
        
    
    def age(self):
        if self.dob[1]<get_date_today()[1]:
            self.age = get_date_today()[0] - self.dob[0] - 1
        elif self.dob[1]<get_date_today()[1] and self.dob[2]<get_date_today()[2]:
            self.age = get_date_today()[0] - self.dob[0] - 1
        else:
            self.age = get_date_today()[0] - self.dob[0] 

def get_date_today():
    return (2013, 10, 30)
       


# Used for public test cases.
# You DO NOT have to include this in your submission
jt = Artist("Justin Timberlake", (1981, 1, 31))
