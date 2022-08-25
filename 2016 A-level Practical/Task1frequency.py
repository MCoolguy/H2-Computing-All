import random


numbers = []

for count in range(1000):
    numbers.append(random.randint(1,20))
    
print("number".ljust(20)+"frequency".ljust(20))

for i in range(1,20):
    print(str(i).ljust(20)+str(numbers.count(i)).ljust(20))
    
    
