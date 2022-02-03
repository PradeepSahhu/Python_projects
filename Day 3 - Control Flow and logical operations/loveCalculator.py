

#Love Calculator...using .lower() and count() function

print("Welcome to love calculator")
name1 = input("Enter your name: ").lower()
name2 = input("Enter her name: ").lower()
lowercase = name1+name2
t = lowercase.count('t')
r = lowercase.count('r')
u = lowercase.count('u')
e = lowercase.count('e')
Ttotal = (t + r + u + e)*10

l = lowercase.count('l')
o = lowercase.count('o')
v = lowercase.count('v')
e = lowercase.count('e')
Tlove = (l + o + v + e)
percentage = Ttotal + Tlove

if(percentage < 10 or percentage > 90):
    print(f"Your score is{percentage}, you go together like coke and mentos")
elif(percentage >=40 and percentage <=50):
    print(f"Your score is {percentage}, you are alright together")
else:
    print(f"Your score is {percentage}")
