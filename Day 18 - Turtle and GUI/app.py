# import bank_account
#
# # from bank_account import BankAccount
#
# print(help("__sizeof__"))
# print(dir(bank_account))
# print(dir(bank_account.BankAccount.deposit))
# print(bank_account.BankAccount.deposit.__sizeof__())
# print(dir(BankAccount))
# print(help("__sizeof__"))
# print(bank_account.BankAccount.__sizeof__())

class MyClass:
    Greetings = ""

    def __init__(self, Name="there"):
        self.Greetings = Name + "!"

    def SayHello(self):
        print("Hello {0}".format(self.Greetings))
        # print("Hello " + self.Greetings)


MyInstance = MyClass("Pradeep Sahu")
print(MyInstance.SayHello())
