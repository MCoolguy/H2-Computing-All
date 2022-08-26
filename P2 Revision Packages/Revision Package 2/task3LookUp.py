
def Hashkey(ThisCountry):
    total = 0 
    for letter in ThisCountry:
        total += ord(letter)
        
    remainder = total % 373
    return remainder +1


file = open("NEWFILE.txt","r")
countries = []
for line in file:
    line = file.readline().strip()
    countrynamepop,address  = line.split(',')
    countries.append([countrynamepop,address])

#print(countries)

countryname = input("Enter country name: ")
countryaddress = Hashkey(countryname)
for i in range(len(countries)-1):
    if int(countries[i][1]) == countryaddress:
        print(countries[i][0]+' '+countries[i][1])
    