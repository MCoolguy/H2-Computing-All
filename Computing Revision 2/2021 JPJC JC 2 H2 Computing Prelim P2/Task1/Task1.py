
def insertionsort(lst):
    for count in range(1,len(lst)):
        temp = count
        while temp > 0 and lst[temp-1]>lst[temp]:
            lst[temp-1],lst[temp] = lst[temp],lst[temp-1]
            temp -=1
            
    return lst

def swapposition(lst):
    lst[0],lst[2] = lst[2],lst[0]
    return lst


    
file = open("marathon.csv","r")
file.readline()

allrunners = []
DNF  = []
sortedrunners = []

for line in file:
    name,country,time = line.strip().split(',')
    allrunners.append([name,country,time])
    if time == "DNF":
        DNF.append([name,country])

finishedrace = len(allrunners) - len(DNF) 
percentage = round((finishedrace/len(allrunners))*100,1)
     
#print("Number of DNF: " + str(len(DNF)))
#print("Total number of athletes: " + str(len(allrunners)))
#print("Percentage of athletes who finished race: " + str(percentage))   
#print(swapposition(allrunners[0]))
for i in range(len(allrunners)-1):
    sortedrunners.append(swapposition(allrunners[i]))
insertionsort(sortedrunners)
#print(sortedrunners)

print("Rank".ljust(20)+"Country".ljust(20)+"Name".ljust(30)+"Timing".ljust(20))
rank = 0
for count in range(20):
    rank +=1 
    print(str(rank).ljust(20)+sortedrunners[count][1].ljust(20)+sortedrunners[count][2].ljust(30)+sortedrunners[count][0].ljust(20))
    

    







file.close()