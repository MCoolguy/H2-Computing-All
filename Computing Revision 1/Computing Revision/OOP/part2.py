class Mammal(object):
    def __init__(self, name):
        self.name = name
       
        
    def get_name(self):
        return self.name
    
    def say(self):
        return "What does the " + str(self.name) +" say" 
        
    
class Dog(Mammal):
    def __init__(self):
        super().__init__(Dog)
        self.name = "Dog"
        
class Dog(Mammal):
    def __init__(self):
        super().__init__("Dog")
    def say(self):
        return "Woof"
    
class Band(Artist):
    def __init__(self, name, dob, members):
        super().__init__(name, dob)
        self.members = members
        
    def formation_age(self):
        return self.age()

    def age(self):
        total_age = 0
        for member in self.members:
            total_age += member.age()

        return total_age / len(self.members)