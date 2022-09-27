
   
class Stack:
    def __init__(self):
        self.S = [[""] for i in range(21)] #Initialise stack
        self.sp = 0 #points to top item in stack

    def isEmpty(self):
         if self.sp ==0:
             return True
         return False
        
    def isFull(self):
        if self.sp ==len(self.S):
            return True
        return False
    
    def push(self,x):
        if self.isFull()==False:
            self.sp +=1 
            self.S[self.sp] = x 
    def pop(self):
        
        if self.sp ==0:
            return None
        temp = self.S[self.sp]
        self.sp -= 1
        return temp
    def peek(self):
        #print(self.S[0])
        return self.S[self.sp]   
#stack = Stack()
#stack.push("omegalul")
#stack.pop()
#stack.push("bruh")
#stack.push("lol")
#stack.push("XD")
#stack.pop()
#print(stack.peek())
def greater(a,b):
    if ((a=='+' or a=='-') and (b=='*' or b=='/' or b =='^')) or ((a=='*' or a=='/')  and b =='^'):
        return True
    return False
    
    

    
def infixtopostfix(infix):
    S = Stack()
    postfix = ""
    for token in infix:
        if token.isalpha():
            postfix += token
        elif token =='(':
            S.push(token)
        elif token ==')':
            while S.pop()!='(':
                postfix += S.pop()
        elif token.isalpha()!=True:
            while S.peek() != "":
                if S.peek() == '(':
                    break
                elif greater(S.peek(),token):
                    postfix += S.pop()
                else:
                    break
            S.push(token)  
            
    while S.peek()!= "":
        postfix += S.pop()
        
    return postfix

print(infixtopostfix("A/(B-C)*D^E"))  
                

