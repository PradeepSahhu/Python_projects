 
#Bmi calculation with labelling...

weight = int(input("Enter your weigh: "))
height = float(input("Enter your height: "))
BMI = round(weight/height**2)
if(BMI < 18.5):
    print(f"Your BMI {BMI}, you are Under Weight")
elif(BMI < 25):
    print(f"your BMI {BMI}, you are a Normal Weight")
elif(BMI < 30):
    print(f"your BMI {BMI}, you are overweight")
elif(BMI < 35):
    print(f"your BMI {BMI}, you are obese.")
else:
    print(f"your BMI {BMI}, you are clinically obese.")
