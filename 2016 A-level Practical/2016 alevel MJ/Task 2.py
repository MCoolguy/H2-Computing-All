def task_2_1():
    Max = 20
    hash_table = [0 for i in range(Max)]

    file = open("KEYS1.TXT", 'r')
    for line in file:
        key = int(line.strip())
        addr = hashing(key, Max)
        hash_table[addr] = key
    file.close()
    return hash_table

def hashing(ID, Max):
    return ID%Max

def task_2_2():
    Max = 20
    hash_table = [0 for i in range(Max)]

    file = open("KEYS2.TXT", 'r')
    for line in file:
        key = int(line.strip())
        addr = hashing(key, Max)
        count = 0
        if hash_table[addr] != 0 and count < Max: #linear probing
            temp_addr = addr + 1
            count += 1
            while hash_table[temp_addr] != 0:
                temp_addr = (temp_addr + 1) % Max
            addr = temp_addr
            
        hash_table[addr] = key
    file.close()
    return hash_table
