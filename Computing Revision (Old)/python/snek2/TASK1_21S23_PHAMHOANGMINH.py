def ValidateScore(Score):
    if Score.isdigit()==False or int(Score)>100:
        return False
    else:
        return True

def main_task():
    file = open("H2MATH2021MYE.txt","r")
    lst = []
    count = 0
    for line in file:
        line.strip()
        lst.append(line)
    print(lst)
     
    for i in range(0,len(lst)):
        if ValidateScore(lst[i])==False:
            count += 1
    return count

         
print(main_task())
     
