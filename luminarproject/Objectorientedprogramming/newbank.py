# bank with staticmethod
import datetime
class Bank:
    bank_name="SBK #static variable"
    def createAccount(self,accno,nam,):
        self.acc=accno
        self.name=nam

        self.balance=3000

    def printBank(self):
        print(self.roll)
        print(self.name)
        print(self.bankname)
        print(self.balance)

    def deposit(self,amount):
     self.balance+=amount
     print("amount ",amount,"credited to your account. availible balance is",self.balance)

    def withdraw(self,amount):
        if(amount>self.balance):
          print("insufficent fund")
        else:
          self.balance-=amount
          print("amount ", amount, "credited to your account. availible balance is", self.balance)

    def balance(self):
        print("your account balance is",self.balance)

obj=Bank()
obj.createAccount(1001,"amal")
obj.deposit(5000)
# obj.withdraw(10000)

# static related to class
