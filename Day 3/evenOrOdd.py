

#Even or odd number using modulo operator.

'''number = int(input("Enter your number: "))
if(number%2==0):
    print(f"{number} is Even number")
else:
    print(f"{number} is odd number")
'''
#Nested if/else statement.

'''height = int(input("Enter your height in cm: "))
if(height >= 120):
    age = int(input("Enter your Age: "))
    if(age >= 18):
        print("your ticket price is $12")
    elif(age < 18 and age >= 12):
        print("your ticket price is $7")
    else:
        print("your ticker price is $5")
else:
   print("you have to grow up in height to take a ride")
'''
#Alternative way without and statement...

if(height >= 120):
    age = int(input("Enter your Age: "))
    if(age < 12 ):
        print("your ticket price is $5")
    elif(age <= 18):
        print("your ticket price is $7")
    else:
        print("your ticker price is $12")
else:
   print("you have to grow up in height to take a ride")
