def bubbleSortScores():
    infile = open("UNSORTEDSCORES.txt","r")
    array = infile.read().splitlines() 
    infile.close()
    array = [ int(i) for i in array ]
    n = len(array)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if array[j] > array[j + 1] :
                array[j], array[j + 1] = array[j + 1], array[j]

    index = (n - 1) // 2
    if (n % 2):
        return array[index]
    else:
        return (float(array[index]) + float(array[index + 1]))/2.0


print(bubbleSortScores())