# import the built-in library timeit 
import timeit 
def task2_1(filename):
    lst = []
    file = open(filename,'r')
    for line in file:
        lst.append(int(line.strip()))
        
    return lst
def task2_2(list_of_integers):
    for i in range(1,len(list_of_integers)):
        key = list_of_integers[i]
        j = i-1
        
        while j>=0 and key<list_of_integers[j]:
            list_of_integers[j+1] = list_of_integers[j]
            j -=1
            
        list_of_integers[j+1] = key
        
    return list_of_integers
# use the function from Task 1.1 to read in 1000 integers from the file THOUSAND.txt 
t1000 = task2_1('THOUSAND.txt')
# use the timeit function to call the task2_2(li) function with the 1000 integer list, run this just once 
time1000 = timeit.timeit(lambda: task2_2(t1000), number=1)
# print out the time, in seconds
print(type(time1000))
