import random
def gen():
    dic = {}
    for i in range(1000):
        data = random.randint(1,20)
        if data not in dic:
            dic[data] = 0
        dic[data] += 1

    #--printing--
    print("{0:10}{1:20}".format("Integer", "Frequency"))
    for i in range(1, 21):
        if i not in dic:
            print( "{0:10}{1:20}".format(str(i) + ':', '0'))
        else:
            print("{0:10}{1:20}".format(str(i) + ':', str(dic[i])))



def gen_2(n, start, end): #ammended gen to meet task 1.2 requirements
    dic = {}
    for i in range(n):
        data = random.randint(start,end)
        if data not in dic:
            dic[data] = 0
        dic[data] += 1
    exp_freq = abs(n/(end-start+1))
    #--printing--
    print("Expected Frequency:", str(exp_freq),'\n')
    print("{0:10}{1:30}".format("Integer", "Frequency Deviation"))
    for i in range(start, end + 1):
        if i not in dic:
            print( "{0:10}{1:20}".format(str(i) + ':', exp_freq))
        else:
            print("{0:10}{1:20}".format(str(i) + ':', str(dic[i]-exp_freq)))

    print("\n'-' denotes that the actual frequency is below expected frequency" )

                  


          
