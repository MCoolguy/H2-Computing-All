def validation(data): #data is given in a tuple form
    #will return False if not valid, True if valid
    if data[1].isnumeric() != True:
        return False
    if type(data[0]) is not str and data[0].isalpha() != True:
        return False
    return True

def input_star():
    name = input("Name of walker (input 'quit' to quit): ")
    steps = input("Number of steps (input 'quit' to quit): ")
    print()
    data = (name, steps)
    if "quit" in data:
        return "quit"
    while validation(data) != True:
        name = input("Name of walker (input 'quit' to quit): ")
        steps = input("Number of steps (input 'quit' to quit): ")
        print()
        data = (name, steps)
        if "quit" in data:
            return "quit"
    return data


def display(lst_name,lst_steps):
    index = lst_steps.index(max(lst_steps))
    print("This week,",lst_name[index],"is 'Star of the Week' with",lst_steps[index],"steps taken.")
    file.close()
    
#=========main program==============

file = open("STAR.TXT", 'r')
lst_name = []
lst_steps = []
for line in file:
    name, steps = line.strip().split(',')
    lst_name.append(name)
lst_steps.append(steps)
index = lst_steps.index(max(lst_steps))
statement = "Last week, " + lst_name[index] + " was 'Star of the Week' with " + lst_steps[index] + " steps taken."
file.close()

file = open("STAR.TXT", 'a')
n = 10 #number of times to input data
lst_name = []
lst_steps = []

for count in range(n):
    data = input_star()
    if data == "quit":
        break
    file.write('\n'+data[0] + ',' + data[1])
    lst_name.append(data[0])
    lst_steps.append(data[1])
    print("Added", data)
    print()

file.close()

print(statement)
display(lst_name, lst_steps)

