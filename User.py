class User:
    active = 0
    def __init__(self,first,last):
        self.name = first
        self.last =last
        User.active +=1


    def get_firstName(self):
        print(self.name)


print(User.active)
user = User("joew","helo")
print(User.active)

# class BankAccount:
#     def __init__(self, owner, balance=0):
#         self.owner = owner
#         self.balance = balance
#
#     def deposite(self,amount):
#         self.balance += amount
#         return self.balance
#
#     def withdraw(self, amount):
#         self.balance -= amount
#         return self.balance
#
#
# acct = BankAccount("Darcy")
# print(acct.owner)
# print(acct.balance)
# acct.deposite(10)
# print(acct.balance)
# acct.withdraw(3)
# print(acct.balance)


