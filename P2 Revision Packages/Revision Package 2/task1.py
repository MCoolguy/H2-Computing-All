#Task 1.1
def task1_1():
    while True:
        letter = input("Enter the alphabetic character ")
        if letter.isalpha()!=True:
            letter = input("Enter a character again, ensure that it is alphabetic: ")
        elif len(letter)>1:
            letter = input("Enter character again, ensure that it is only one character")
        
        break

    return letter

#Task 1.2
def task1_2(letter,base):
##    letter = input("Enter a letter: ")
##    while True:
##        base = input("Enter a number base greater than 10 less than 16: ")
##        if (int(base)>16) or (int(base)<10):
##            base = input("Enter a number base greater than 10 less than 16: ")
##        break

    asciivalue = ord(letter)
    base = int(base)
    #print(asciivalue)

    finalbase = ""

    quotient = asciivalue //base
    remainder = asciivalue % base
    finalbase += str(remainder)
    while quotient>0:
        remainder = quotient % base
        quotient = quotient //base
        finalbase += str(remainder)
    return finalbase[::-1]
##
##print("Letter".ljust(20)+letter)
##print("Denary".ljust(20)+str(asciivalue))
##print("Numberbase".ljust(15)+str(base).ljust(5)+str(finalbase[::-1]))
    
#Task 1.3
while True:
    print("1. Enter a letter \n2. Convert to Denary \n3. Convert to Base 11 \n4. Convert to Base 12 \n5. Convert to Base 13 \n6. Convert to Base 14\n7. Quit") 
    userinput = input("Choice: ")
    if userinput =="7":
        break
    elif userinput == "1":
        letter = task1_1()
    elif userinput =="2":
        print(ord(letter))
    elif userinput == "3":
        print(task1_2(letter,11))
    elif userinput == "4":
        print(task1_2(letter,12))
    elif userinput == "5":
        print(task1_2(letter,13))
    elif userinput == "6":
        print(task1_2(letter,14))
        
        
    
    


