
hexa =['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
while True:
    hexanumber = input("enter hexadecimal number ")
    for i in hexanumber:
        #print(i)
        if (i not in hexa): 
            hexanumber = input("enter hexadecimal number again ")
    break
            
            
def hextoden(hex):
    sum = 0
    power = 0
    hex=hex[::-1]
    for i in hex:
        sum += hexa.index(i) * (16**power)
        power +=1 
        
    return sum

#print(hextoden(hexanumber) )   

def dentohex(den):
    den = int(den)
    hexanum = ""
    if den == 0:
        return 0 
    else:
        while den>0:
            remainder = den%16
            quotient = den //16
            hexanum += hexa[remainder]
            den = quotient
    return hexanum[::-1]

print(dentohex(hexanumber))
            
    
    
    
 