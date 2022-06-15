# Making a Class with proper structure.

class BankAccount:
    """
    Class to simulate Bank Account
    Attributes :
        Balance : to hold balance amount in the bank
    """

    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance = self.balance + amount
        return self.balance

    def withdraw(self, amount):  # Don't add self of the parameter value. like here: amount
        if self.balance < amount:  # self are only added to  the attributes element
            return "insufficient balance in your account"
        self.balance = self.balance - amount
        return self.balance


# ac123 = BankAccount()
# print(ac123.balance)
# ac123.deposit(10000)
# ac123.withdraw(2000)
# print(ac123.balance)
# ac123.deposit(10000)
# print(ac123.withdraw(100000))
