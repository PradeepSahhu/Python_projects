
#For loops.
'''
fruit = ["Apple", "mango","Banana", "Orange","Melon","papaya"]
for f in fruit:
    print(f)
'''
'''student_heights = input("Enter height of students ").split()
num = 0
for heights in student_heights:
    heights = int(heights)
    num+=heights
    avg = num/len(student_heights)
print(round(avg,2))
'''

#Without using len() and sum() function.
student_heights = input("Enter height of students ").split()

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

num = 0
height = 0
for total_height in student_heights:
    num+=1
    height+=total_height
    avg = round(height/num)
print(avg)
