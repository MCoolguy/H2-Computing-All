def bubble(lst):
    n = len(lst)
    for i in range(1,n):
        for j in range(n-1):
            if lst[j]>lst[j+1]:
                lst[j],lst[j+1] = lst[j+1], lst[j]
                
    print(lst)

def insert(lst):
    n = len(lst)
    for i in range(1,n):
        j = i 
        while j>=0 and lst[j]<lst[j-1]:
            lst[j],lst[j-1] = lst[j-1],lst[j]
            j-=1
            
    print(lst)


def mergesort(lst):
    n = len(lst)
    if n ==1:
        return lst
    
    left = lst[:n//2]
    right = lst[n//2:]
    
    left = mergesort(left)
    right = mergesort(right)
    
    return merge(left,right)


    
        
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

    







lst=[4,3,1,6,8,2,7,1]
print(mergesort(lst))