

#strings

'''num = str(len(input("enter your name ")))
print("Your name has "+ num +" characters") #now after using str() num datatype has converted to string and now it can concatenate...
'''
#Sum for two digit numbers...
'''num = int(input("Enter your fav 2 digit number")) #input returns str type data...
num_string = str(num)
num1 = num_string[0]
num2 = num_string[1]
print(int(num1)+int(num2))
'''


#sum for any digit of numbers...
'''num = int(input("Enter your fav number: "))
num_string = str(num)
start = 0
for i in range(0, len(num_string)):
    start+=int(num_string[i])
print(start)'''
    
