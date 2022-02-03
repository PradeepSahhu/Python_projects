
#Dictionaries 

student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}


#TODO-2: Write your code below to add the grades to student_grades.👇
for scores in student_scores:
    #print(student_scores[scores])
    numbers = student_scores[scores]
    if(numbers >= 91):
        student_grades[scores] = "Outstanding"
    elif(numbers >= 81):
        student_grades[scores] = "Exceeds Expectations"
    elif(numbers >= 71):
        student_grades[scores] = "Acceptable"
    elif(numbers <= 70):
        student_grades[scores] = "Fail"
        
    
    

    

# 🚨 Don't change the code below 👇
print(student_grades)
