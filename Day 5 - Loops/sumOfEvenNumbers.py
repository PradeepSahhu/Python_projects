
# Sum of Even Numbers.
'''
total = 0
for number in range(1,101):
    if(number%2 == 0):
        total+=number
print(total)
'''
#Alternative way...

total = 0
for number in range(2,101,2): #start, end and step.
    total+=number
print(total)

