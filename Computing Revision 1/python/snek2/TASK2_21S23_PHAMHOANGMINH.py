
# coding: utf-8

# In[62]:


file = open("ADMISSIONS.txt","r")
infile = file.readlines()
list1 = []
lst = []
for line in infile:
    list1 += line.split()
n = len(list1)
file.close()
for i in range(0,n):
    lst.append(int(list1[i]))
m = len(lst)    
for i in range(m-1):
    for j in range(0,m-i-1):
        if lst[j]>lst[j+1]:
            lst[j],lst[j+1] = lst[j+1], lst[j]
            
    


# In[43]:


def bubblesort(lst):
    for i in range(0,len(lst)-2):
        posn = 0
        noswap = True
        while True:
            if posn == len(lst) - i -1:
                break
            if lst[posn] > lst[posn+1]:
                noswap = False
                temp = lst[posn]
                lst[posn] = lst[posn+1]
                lst[posn+1] = temp
            else:
                posn = posn +1
        if noswap == True:
            return lst
    return lst

def task2_1(list_of_integers):
        finallst = bubblesort(lst)
        return finallist


# In[45]:


def bubblesort(lst):
    for i in range(0,len(lst)-2):
        posn = 0
        noswap = True
        while True:
            if posn == len(lst) - i -1:
                break
            if lst[posn] > lst[posn+1]:
                noswap = False
                temp = lst[posn]
                lst[posn] = lst[posn+1]
                lst[posn+1] = temp
            else:
                posn = posn +1
        if noswap == True:
            return lst
    return lst

def task2_2(filename_in,filename_out):
    file = open(filename_in,"r")
    infile = file.readlines()
    list1 = []
    lst = []
    for line in infile:
        list1 += line.split()
    n = len(list1)
    for i in range(0,n):
        lst.append(int(list1[i]))
    finallist = bubblesort(lst)
    file.close()
    file2 = open(filename_out,"w")
    file2.write(str(finallist))
    file2.close()
    

task2_2("ADMISSIONS.txt","SORTED.txt")


# In[64]:


file = open("SORTED.txt","r")
infile = file.readlines()
lst = infile[0]
lst = lst.replace("[","")
lst = lst.replace("]","")
count = 0
for i in range(0,len(lst)):
    if int(lst[i]) <5000:
        count += 1
print(count)

