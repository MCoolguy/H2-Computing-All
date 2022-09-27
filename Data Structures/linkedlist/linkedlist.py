Data = [""for i in range(51)]
Ptr = [""for i in range(51)]

def InsertListItem(email):
    global StartPtr, NextFree, Ptr
    if NextFree == 0:
        return "UNSUCCESSFUL"
    
    Data[NextFree] = email
    temp_pointer = StartPtr
    first_flag = True
    while temp_pointer != 0:
        previous = temp_pointer
        temp_pointer = Ptr[temp_pointer]
        first_flag = False
        
    if first_flag == True:
        Ptr[NextFree] = 0
        StartPtr = 1
    else:
        Ptr[previous] = NextFree
        Ptr[NextFree] = 0
    
    NextFree += 1
    return "INSERTED"

def DeleteListItem(email): #delete node with surname
    global StartPtr
    temp_pointer = StartPtr
    previous = temp_pointer
    while Data[temp_pointer] != email and temp_pointer != 0:
        previous = temp_pointer
        temp_pointer = Ptr[temp_pointer]
        
    if temp_pointer == 0 and Data[temp_pointer] != email:
        return "UNSUCCESSFUL"
    
    elif Data[temp_pointer] == email and temp_pointer != 0:
        Ptr[previous] = Ptr[temp_pointer]
    
    else:
        Ptr[previous] = 0
    return "DELETED"

def traversal():
    global StartPtr
    #your code here
    temp_lst = []
    if StartPtr == 0:
        return temp_lst
    
    temp_pointer = StartPtr
    previous = temp_pointer
    while temp_pointer != 0:
        temp_lst.append(Data[temp_pointer])
        temp_pointer = Ptr[temp_pointer]
    return temp_lst
