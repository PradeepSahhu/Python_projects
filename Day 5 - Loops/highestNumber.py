

#higest number in a list.

#Works for all the positive integers...
''' 
student_score = input("Enter the numbers in the list ").split()

for n in range(0,len(student_score)):
    student_score[n] = int(student_score[n])
print(student_score)

highest = 0
for num in student_score:
    if(num > highest):
        highest = num   #no double equal sign (==) single equal to assign and double equal to check.
print(highest)

'''
#for all the negative integers.
student_score = input("Enter the numbers in the list ").split()

for n in range(0,len(student_score)):
    student_score[n] = int(student_score[n])
print(student_score)

highest = student_score[0]
for num in student_score:
    if(num > highest):
        highest = num   #no double equal sign (==) single equal to assign and double equal to check.
print(highest)
