def binarysearch(list1, target):
    left = 0
    right = len(list1) - 1
    while left <= right:
        mid = (left + right) // 2 # make sure to round it down
        if list1[mid] == target:
            return mid
        elif target < list1[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return "aint here bruv"

def linearsearch(list1,target):
    for i in range(len(list1)):
        if list1[i] == target:
            return i 
    return "it aint here bruv"



testlist = [1,2,3,4,5,6,7,8]

#print(binarysearch(testlist,8))
print(linearsearch(testlist,7))