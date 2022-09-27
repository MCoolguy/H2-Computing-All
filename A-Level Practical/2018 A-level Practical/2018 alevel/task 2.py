def QuickSort(Scores):
    QuickSortHelper(Scores, 0, len(Scores)-1)
    return Scores


def QuickSortHelper(Scores, First, Last):
    if First < Last:
        SplitPoint = Partition(Scores, First, Last)
        QuickSortHelper(Scores, First, SplitPoint -1)
        QuickSortHelper(Scores, SplitPoint+1, Last)
    return Scores


def Partition(Scores, First, Last):
    PivotValue = Scores[First]
    LeftMark = First + 1
    RightMark = Last
    Done = False
    while Done == False:
        while LeftMark <= RightMark and Scores[LeftMark] <= PivotValue:
            LeftMark += 1
        while Scores[RightMark] >= PivotValue and RightMark >= LeftMark:
            RightMark -= 1
        if RightMark < LeftMark:
            Done = True
        else:
            Temp = Scores[LeftMark]
            Scores[LeftMark] = Scores[RightMark]
            Scores[RightMark] = Temp
            
    Temp = Scores[First]
    Scores[First] = Scores[RightMark]
    Scores[RightMark] = Temp

    return RightMark


def display(data):
    print("Before quick sort:", data)
    sorted_data = QuickSort(data)
    print("After quick sort:", sorted_data)
    return




#========main program==========
lst = [72,45,57,76,29,40,42,77,64,91,24,92,73,78,62,27,26,67,34,20,90,75,89,98,41,37,58]
display(lst)

        
