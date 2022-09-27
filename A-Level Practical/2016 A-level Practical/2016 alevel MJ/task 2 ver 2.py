def gen_addr(ID, Max):
    return ID % Max

def task2_1(Max = 20):
    #assumption: no collision
    file = open("KEYS1.TXT", 'r')
    hash_table = [0 for i in range(Max)] #0-based indexing array

    for line in file:
        ID = int(line.strip())
        addr = gen_addr(ID, Max)
        hash_table[addr] = ID

    file.close()
    display(hash_table)

def display(arr):
    print("Order of storing: ")
    for item in arr:
        if item != 0:
            print(item)


def task2_2(Max = 20):
    file = open("KEYS2.TXT", 'r')
    hash_table = [0 for i in range(Max)] #0-based indexing array

    for line in file:
        ID = int(line.strip())
        addr = gen_addr(ID, Max)
        
        if hash_table[addr] != 0: #linear probing
            temp_addr = addr
            count = 0
            while hash_table[temp_addr] != 0 and count != 20:
                temp_addr = (temp_addr +1 )%20
                count += 1
            addr = temp_addr
        
        hash_table[addr] = ID

    file.close()
    display(hash_table)
    return hash_table


def hashing(ID, hash_table, Max):
    addr = gen_addr(ID, Max)
    if hash_table[addr] != 0: #linear probing
        temp_addr = addr
        count = 0
        while hash_table[temp_addr] != 0 and count != 20:
            temp_addr = (temp_addr +1 )%20
            count += 1
        addr = temp_addr
    hash_table[addr] = ID
    return hash_table

def task2_3(Max = 20, input_no = 3):
    hash_table = [0 for i in range(Max)] #0-based indexing array

    for i in range(input_no):
        ID = int(input("ID?: "))
        hash_table = hashing(ID, hash_table, Max)
    
    display(hash_table)
    return hash_table

