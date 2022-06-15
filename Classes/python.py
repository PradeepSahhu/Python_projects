class MyClass:
    def __init__(self, *args):
        self.Input = args
    def __add__(self, Other):
        Output = MyClass()
        Output.Input = self.Input + Other.Input
        '''print(self.Input)
        print(Other.Input)
        print(Output)'''
        print(type(Output))
        return Output
    def __str__(self):
        Output = ""
        '''print(self.Input)
        print(type(self.Input))'''
        for Item in self.Input:
            Output += Item
            Output += " "
            '''print(Output)
        print(type(Output))'''
        
        return Output
Value1 = MyClass("Red", "Green", "Blue")
Value2 = MyClass("Yellow", "Purple", "Cyan")
Value3 = Value1 + Value2

print("{0} + {1} = {2}"
      .format(Value1, Value2, Value3))
'''
print(type(Value1))
print(type(Value2))
print(type(Value3))

value4 = ("hello", "there", "good-bye")
value5= ("SOrry", "Thankyou", "No problem")
value6 = value4 + value5
print(value6)
print(type(value6))
'''
