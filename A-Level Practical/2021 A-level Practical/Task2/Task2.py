import timeit 


def task2_1(filename):
    lst = []
    file = open(filename,'r')
    for line in file:
        lst.append(int(line.strip()))
        
    return lst

#result = task2_1('TEN.txt')
# print(result)
# print(len(result))


def task2_2(list_of_integers):
    for i in range(1,len(list_of_integers)):
        key = list_of_integers[i]
        j = i-1
        
        while j>=0 and key<list_of_integers[j]:
            list_of_integers[j+1] = list_of_integers[j]
            j -=1
            
        list_of_integers[j+1] = key
        
    return list_of_integers

#print(task2_2(task2_1('TEN.txt')))

def partition(list_of_integers,low,high): #quicksort partitionhelper
    i = low
    pivot = list_of_integers[high]
    for j in range(low,high):
        if list_of_integers[j]<=pivot:
            list_of_integers[j],list_of_integers[i] = list_of_integers[i],list_of_integers[j]
            i+=1
    
    list_of_integers[high],list_of_integers[i] = list_of_integers[i],list_of_integers[high] 
    
    return i 
    
    
    
def task2_3_helper(list_of_integers,low,high):
    if low<high:
        partition_index = partition(list_of_integers,low,high)
        task2_3_helper(list_of_integers,low,partition_index-1)
        task2_3_helper(list_of_integers,partition_index+1,high)
        
    return list_of_integers

def task2_3(list_of_integers):
    low = 0
    high = len(list_of_integers) -1
    return task2_3_helper(list_of_integers,low,high)


#print(task2_3(task2_1("TEN.txt")))


insertion_timings = []
quicksort_timings = []


t10= task2_1('TEN.txt')
t100 = task2_1('HUNDRED.txt')
t1000 = task2_1('THOUSAND.txt')
insertion_timings.append(timeit.timeit(lambda: task2_2(t10), number=1))
insertion_timings.append(timeit.timeit(lambda: task2_2(t100), number=1))
insertion_timings.append(timeit.timeit(lambda: task2_2(t1000), number=1))
#print(insertion_timings)

quicksort_timings.append(timeit.timeit(lambda: task2_3(t10), number=1))
quicksort_timings.append(timeit.timeit(lambda: task2_3(t10), number=1))
quicksort_timings.append(timeit.timeit(lambda: task2_3(t10), number=1))
#print(quicksort_timings)

for index in range(3):
    if index ==0:
        length = 10
    elif index ==1:
        length = 100
    elif index ==2:
        length =1000
        
    if insertion_timings[index]< quicksort_timings[index]:
        print("Insertion is faster for lists of length "+ str(length))
    else:
        print("Quicksort is faster for lists of length "+ str(length))






        
    