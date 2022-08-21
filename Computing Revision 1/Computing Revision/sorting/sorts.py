

def bubblesort(list1):
    for i in range(1,len(list1)):
        for j in range(0,len(list1)-1):
            if list1[j]>list1[j+1]:
                list1[j],list1[j+1] = list1[j+1],list1[j]
                               
    print(list1) 
    
    
def insertionsort(list1):
    for i in range(1,len(list1)):
        j = i 
        while j>0 and list1[j-1]>list1[j]:
            list1[j-1],list1[j] = list1[j],list1[j-1]
            j -=1   
              
    print(list1)
            
            
def merge(left,right):
    finallist = []
    while len(left)!=0 and len(right) != 0:
        if left[0]>right[0]:
            finallist.append(right[0])
            right.pop(0)
        else:    
            finallist.append(left[0])
            left.pop(0)
            
    while len(left)!=0:
        finallist.append(left[0])
        left.pop(0)
    while len(right)!=0:
        finallist.append(right[0]) 
        right.pop(0)  
        
    return finallist         
            
def mergesort(list1):
    n = len(list1)
    if n==1:
        return list1
    
    left = list1[:n//2]
    right = list1[n//2:]
    
    left = mergesort(left)
    right = mergesort(right)
    
    return merge(left,right)


def partition(list, low, high):
    i = low
    pivot = list[high]

    for j in range(low, high):
        if list[j] <= pivot:
            list[i], list[j] =  list[j], list[i]
            i += 1

    list[i], list[high] = list[high] ,list[i]

    return i

def quicksort(list, low, high):
    if low < high:
        partition_index = partition(list, low, high)
        quicksort(list, low, partition_index - 1)
        quicksort(list, partition_index + 1, high)
    

    
#### Main program ####
testlist = [2,7,3,5,9,1,4,6,1,2,8]
#insertionsort(testlist)
#bubblesort(testlist)
print(mergesort(testlist))
#quicksort(testlist,0,len(testlist)-1)
#print(testlist)