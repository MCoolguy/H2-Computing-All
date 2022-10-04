def task1_1(input_value):
    if input_value.isnumeric()!=True or len(input_value)!=14:
        return -1
    
    input_value = input_value[::-1]
    total = 0
   
    for index in range(0,len(input_value)):
        if index%2==0:
            double = int(input_value[index])*2
            for number in str(double):
                total += int(number)
        
        else:
            total += int(input_value[index])
    

    for count in range(0,9):
        if (total + count)%10==0:
            return count
        
        

# print(task1_1('14576567654934'))
# print(task1_1('1457656765493A'))
# print(task1_1('145765676549348'))
# print(task1_1('145765676559348'))

def task1_3(input_value):
    if input_value.isnumeric()!=True or len(input_value)!=15:
        return False
    
    checkdigit = int(input_value[-1])
    correctdigit = task1_1(input_value[0:14])
    return checkdigit == correctdigit


print(task1_3('145765676549342'))
    
