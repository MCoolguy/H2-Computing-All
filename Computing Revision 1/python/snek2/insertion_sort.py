
def minRainfall(array):
    return array[0]

    

def maxRainfall(array):
    return array[-1]
    

def medianRainfall(array):
    arrlen = len(array)
    index = (arrlen - 1) // 2
    if (arrlen % 2):
        return array[index]
    else:
        return (float(array[index]) + float(array[index + 1]))/2.0
    

def sortRainfall():
    infile = open("RAINFALL.txt","r")
    array = infile.read().splitlines() 
    infile.close()
    array = [ float(i) for i in array ]
    for i in range(1,len(array)):
        key = array[i]
        j = i - 1
        while j>= 0 and key<array[j]:
            array[j+1] = array[j]
            j = j -1
        array[j+1] = key
    return array 

print(sortRainfall())   
    
    
#DO NOT DELETE THE LINES BELOW
#=============================

sortedarray = sortRainfall()
minRain = minRainfall(sortedarray)
maxRain = maxRainfall(sortedarray)
medianRain = medianRainfall(sortedarray)