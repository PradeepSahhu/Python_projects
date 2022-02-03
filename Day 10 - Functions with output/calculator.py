

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


num1 = int(input("Enter your First Number: "))
num2 = int(input("Enter your second Number: "))

for operators in operations:
    print(operators)

operation_symbol = input("Enter your operator: ")
function = operations[operation_symbol]
answer = function(num1, num2)
print(f"{num1} {operation_symbol} {num2} = {answer}")


    
    
