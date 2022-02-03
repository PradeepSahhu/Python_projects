
#Prime-number checker.

def prime_checker(number):
    is_prime = True
    for num in range(2, number):
        if(number%num == 0):
            is_prime = False
    if is_prime: #it means is_prime == True
        print("It's a prime number")
    else:
        print("It's not a prime numbe")



#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
