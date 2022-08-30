import random
def task1_1():
    dic = {}
    for i in range(1000):
        num = random.randint(1,20)
        if num not in dic:
            dic[num] = 0 #instantiates new dictionary key
        dic[num] += 1

    #----------printing---------------
    print("{0:10}{1:20}".format("Integer", "Frequency"))

    for i in range(1,21):
        freq = 0
        if i in dic:
            freq = dic[i]
        print("{0:10}{1:20}".format(str(i) + ':', str(freq)))



def task1_2(n, start, end):
    dic = {}
    for i in range(n):
        num = random.randint(start,end)
        if num not in dic:
            dic[num] = 0 #instantiates new dictionary key
        dic[num] += 1

    exp_freq = abs(n/(end-start+1) )
    print("Expected Frequency:", str(exp_freq))
    print("{0:10}{1:20}".format("Integer", "Deviated Frequency"))

    for i in range(1,21):
        freq = 0
        if i in dic:
            freq = dic[i]
        print("{0:10}{1:20}".format(str(i) + ':', str(round(freq-exp_freq,1) ) ) )

    print("\n'-' denotes actual freqency is below expected frequency")
