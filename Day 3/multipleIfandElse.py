
height = int(input("Enter your height "))
bill = 0
if(height >= 120):
    age = int(input("Enter your Age: "))
    if(age < 12 ):
        bill = 5
        print(f"Child ticket is ${bill}")
    elif(age <= 18):
        bill = 7
        print(f"Youth ticket price is ${bill}")
    else:
        bill = 12
        print(f"Adult ticker price is ${bill}")
    wants_photo = input("Do you want to take a photo Y or N?")
    if(wants_photo =="y"):
        bill+=3
    print(f"Your final bill is ${bill}. ")
else:
   print("you have to grow up in height to take a ride")

