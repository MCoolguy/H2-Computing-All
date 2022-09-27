def validate(data):
    hex_list = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','a','b','c','d','e','f']
    for item in data:
        if item not in hex_list:
            return False
    return True


def hex_to_den(data, exp = -1):
    hex_list = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    if exp == -1:
        exp = len(data)-1
    if exp == 0:
        return hex_list.index(data[0])
    return hex_list.index(data[0])*(16**(exp)) + hex_to_den(data[1:], exp-1)


def input_hex():
    data = input("Input hex num:" )
    if validate(data):
        return data, hex_to_den(data)

    print("Invalid input")
    return data, "NULL"

#======main program=========

#task 4.2
lst = []
for count in range(3):
    hex_num, den_num = input_hex()
    lst.append([hex_num, den_num])


print("{0:30}{1:40}{2:30}".format("Hexadecimal number", "Purpose of the test", "Expected Output"))
for item in lst:
    hex_num = item[0]
    if validate(hex_num):
        den_num = str(int(hex_num,16))
    else:
        den_num = "NULL"
    
    purp = "Normal test"
    if den_num == "NULL":
        purp = "Errorneous test"

    if hex_num == "0":
        purp = "Boundary test"
    
    print("{0:30}{1:40}{2:30}".format(hex_num, purp, den_num))



print("\nActual run")
print("{0:7}{1:7}".format("hex", 'den'))
for item in lst:
      print("{0:7}{1:7}".format(item[0], str(item[1])))

print()

#task 4.3
def den_to_hex(num):
    if num == 0:
        return ''
    hex_list = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    return den_to_hex(num//16) + hex_list[num%16]

def validate_den(data):
    if data.isnumeric():
        return True
    return False
def input_den():
    data = input("Input denary: ")
    if validate_den(data):
        hex_num = den_to_hex(int(data))
        return hex_num, data
    return "NULL", data

#task 4.4
lst = []
for count in range(3):
    hex_num, den_num = input_den()
    lst.append([hex_num, den_num])

print("{0:30}{1:40}{2:30}".format("Denary number", "Purpose of the test", "Expected Output"))
for item in lst:
    den_num = item[1]
    if validate_den(den_num):
        den_num = int(den_num)
        hex_num = hex(den_num)[2:]
    else:
        hex_num = "NULL"
    
    purp = "Normal test"
    if hex_num == "NULL":
        purp = "Errorneous test"

    if den_num == 0:
        purp = "Boundary test"
    
    print("{0:30}{1:40}{2:30}".format(str(den_num), purp, hex_num))

print("\nActual run")
print("{0:7}{1:7}".format("den", 'hex'))
for item in lst:
      print("{0:7}{1:7}".format(str(item[1]), item[0]))
