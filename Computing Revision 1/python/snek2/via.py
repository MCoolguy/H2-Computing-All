def validate(x):
    if x.isdigit() and int(x)>=1:
        return True
    return False

x = input("What is the minimum number of via hours? ")
while not validate(x):
    x = input("What is the minimum number of via hours? ")
x = int(x)
linenumber = 0
count = 0
data = []
infile = open("VIA.txt",'r')
for line in infile:
    line = line.strip()


    if linenumber%2==0:
        name = line
    else:
        selfi,schooli,other = line.split(":")
        hours = int(selfi)+int(schooli)+int(other)
        if hours<x:
            count +=1
        data.append ((hours,name))
    linenumber+=1
infile.close()
data.sort()
print("{0} out of {1} students did not complete {2} hours of VIA.".format(count,len(data),x))
for item in data:
    if item[0]<x:
        print("{0},{1}".format(item[0], item[1]))

