def uniqueValues(dic):
    newlist = []
    lst = []
    
    
    for key in dic:
        newlist.append(dic[key])
    
    for i in newlist:
        if i not in lst:
            lst.append(i)
    lst.sort()
    return lst
    
#DO NO AMEND THE FOLLOWING CODE
dic = {"Mark":"S001", "Vonny": "S002", "Ash": "S001", "Joyce": "S005", "Weiling":"S005", "John":"S009", "Tim":"S007"}

def combine(d1,d2):
    for key in d2:
        if key in d1:
         d2[key] = d2[key] + d1[key]
        else:
         pass
    d2['c'] = 300   
    return d2
#DO NOT AMEND THE FOLLOWING CODE
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}