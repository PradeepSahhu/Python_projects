#importing module.
import art


#calculator


#Add
def add(n1, n2):
    return n1 + n2

#Subtract
def subtract(n1, n2):
    return n1 - n2

#Multiply
def multiply(n1, n2):
    return n1 * n2

#Divide
def divide(n1, n2):
    return n1 / n2


operations = {"+": add,"-":subtract,"*":multiply,"/":divide}

def calculation():
    print(art.logo)
    num1 = float(input("Enter your First Number: "))


    for operators in operations:
        print(operators)

    more_operations = True
    while more_operations:
        operation_symbol = input("Pick an operator: ")
        num2 = float(input("Enter next Number: "))
        function = operations[operation_symbol]
        answer = function(num1, num2)
        print(f"{first_answer} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {first_answer}, or type 'n' start a new calculation :").lower() == "y":
            num1 = answer
        else:
            more_operations = False
            #Recursion. function calling itself under certain conditions, if condition is not given then it will be infinite loop.
            calculation()
    

calculation()
    


    
    
