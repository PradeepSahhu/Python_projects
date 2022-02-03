
#Palindrome.

number = int(input("Enter your digits"))
temp = number
rev = 0
while number > 0 :
    dig = number % 10
    rev *= 10 + dig
    number = number // 10
if temp == number:
    print(f"is a Palindrome")
else:
    print(f"Not a palindrome")
    
