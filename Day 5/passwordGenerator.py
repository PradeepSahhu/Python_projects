
#Random Password Generator...

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Easy password in sequence.
'''password = ''
for number in range(0,nr_letters):
    password += letters[random.randint(0,len(letters)-1)]  #random.choice(letters)
for number2 in range(0,nr_symbols):
    password += symbols[random.randint(0,len(symbols))-1]
for number3 in range(0,nr_numbers):
    password += numbers[random.randint(0,len(numbers))-1]
        
print(password)
'''
#Hard password sequence...
password = []
for number in range(0,nr_letters):
    #password.append()also works to add character in list.
    password += letters[random.randint(0,len(letters)-1)]  #random.choice(letters)
for number2 in range(0,nr_symbols):
    password += symbols[random.randint(0,len(symbols))-1]
for number3 in range(0,nr_numbers):
    password += numbers[random.randint(0,len(numbers))-1]

#Randamize the password list
random.shuffle(password)

#turn to back into string from list
password_str = ""
for char in password:
    password_str += char
        
print(password_str)
    
    
