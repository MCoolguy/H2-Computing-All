def Hashkey(ThisCountry):
    total = 0 
    for letter in ThisCountry:
        total += ord(letter)
        
    remainder = total % 373
    return remainder +1

#print(Hashkey("India"))
symbols = [" ",".","-",",","","'",'&']
def CreateCountry():
    file = open("COUNTRIES.txt",'r')
    countries = []
    for line in file:
        line = file.readline().strip()
        #print(line)
        countryname = ""
        countrypop = "" 
        while True:
            for count in range(len(line)):
                if line[count].isdigit():
                    break
                else:
                    
                    countryname += line[count]
            countrypop =line[count:] #remaining line[count] is the population
            #print(countryname)
            countryname = countryname[:-1] #removes space at the end 
            address = Hashkey(countryname)
            break
        countries.append([countryname+" "+countrypop,address])
        
    file2 = open("NEWFILE.txt",'w')
    for i in range(len(countries)-1):
        #print(countries[i])
        #file2.write(' '.join([str(item) for item in countries[i]])+"\n")
        countryandpop = str(countries[i][0])
        hashaddress = str(countries[i][1])
        file2.write(countryandpop+","+hashaddress+'\n')
# for list in countries:
#     for item in list:
#         file2.write(str(item)+'\n')
  
    file.close()
    file2.close()