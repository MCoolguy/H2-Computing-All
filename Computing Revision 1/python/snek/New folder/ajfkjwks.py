def remove_extras(lst):
    new_lst = []
    count = 0
    for i in lst:
        if i not in new_lst:
            new_lst.append(i)
            count += 1
    lst = lst + new_lst
    lst = lst[count:-1]
    return lst
    

   
lst1 = [1, 5, 1, 1, 3]
result1 = remove_extras(lst1)
print(result1)
  
# Do not remove the following code
#lst2 = [2, 2, 2, 1, 5, 4, 4]
#result1 = remove_extras(lst1)
#result2 = remove_extras(lst2)
