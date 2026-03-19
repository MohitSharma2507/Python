
#! Abstraction
# Hiding the implementation details of class and only showing the essectial features to the user

#! Encapsulation
#  Wrapping data and functions into a single unit (object) 

class Account:
    def __init__(self,bal,acc):
        self.balance = bal
        self.account_no = acc

    def debit(self,amount):
        self.balance -=amount
        print("Rs. ",amount," is debited")
        print("total balance = ",self.get_balance())

    def credit(self,amount):
        self.balance +=amount
        print("Rs. ",amount," is credited")
        print("total balance = ",self.get_balance())

    def get_balance(self):
        return self.balance
    
acc1 = Account(10000,12345)
acc1.debit(2000)
acc1.credit(5000)