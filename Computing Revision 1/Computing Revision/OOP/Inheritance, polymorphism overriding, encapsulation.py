class BankAccount:
       def __init__(self):
              self.__interestRate = 0.03
              self.__accountId = ""
              self.__balance = 0.0
       def getInterestRate(self):
              return self.__interestRate
       def setInterestRate(self, newIR):
              self.__interestRate = newIR
       def getAccountId(self):
              return self.__accountId
       def setAccountId(self, newId):
              self.__accountId = newId
       def getBalance(self):
              return self.__balance
       def setBalance(self, newBalance):
              self.__balance = newBalance
       def deposit(self, amount):
              self.setBalance(self.getBalance() + amount)
       def withdraw(self, amount):
              if amount <= self.getBalance():
                     self.setBalance(self.getBalance() - amount)
                     return True
              return False
       def accumulateInterest(self):
              self.setBalance(self.getBalance() + (self.getBalance() * self.getInterestRate()))
       def toString(self):
              print("Account Id".ljust(12)+"Balance".ljust(12)+"Interest Rate")
              print(self.getAccountId().ljust(12)+str(self.getBalance()).ljust(12)+str(self.getInterestRate()))
              print()
              
class JuniorAccount(BankAccount):
    def __init__(self):
       self.interestRate = 0.04
       self.accountId = ""
       self.balance = 0.0
        
        
    def getInterestRate(self):
            return self.interestRate
    def setInterestRate(self, newIR):
            self.interestRate = newIR
    def getAccountId(self):
            return self.accountId
    def setAccountId(self, newId):
            self.accountId = newId
    def getBalance(self):
            return self.balance
    def setBalance(self, newBalance):
            self.balance = newBalance
    def deposit(self, amount):
            self.setBalance(self.getBalance() + amount)
    def withdraw(self, amount):
            if amount <= self.getBalance() and amount<=50:
                    self.setBalance(self.getBalance() - amount)
                    return True
            return False
    def accumulateInterest(self):
            self.setBalance(self.getBalance() + (self.getBalance() * self.getInterestRate()))
    def toString(self):
            print("Account Id".ljust(12)+"Balance".ljust(12)+"Interest Rate")
            print(self.getAccountId().ljust(12)+str(self.getBalance()).ljust(12)+str(self.getInterestRate()))
            print()  