#mathematical operations

weight = float(input("Enter your weight in KG: ")) #only input will return value in string.
height = float(input("Enter your height in M: "))#thats why i use float...
BMI = int(weight/(height**2)) #BMI will be in integer...
if (BMI > 23.9):
    print("Your bmi is :", BMI, "You are overweight")
elif (BMI > 18 and BMI < 23.9):
    print("your bmi is : ", BMI, "you are normal weight")
else:
    print("your bmi is :", BMI, "you are underweight")

