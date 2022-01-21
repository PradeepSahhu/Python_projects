

#tip calculator.
'''money = float(input("Enter your Amount: $" ))
interest = int(input("Enter your interest rate 6%, 12% or 18%: "))
friends = int(input("Enter your friends: "))

money += (money*(interest/100)) #or *1.06, 1.12 or 1.18 because sum is exactly 1 and 0.12 is interest rate.
finalAmount = money/friends
finalAmount = "{:.2f}".format(finalAmount) #will format every decimal upto two decimal place...
print(f"you each have to pay {finalAmount} because your total amount is {money}")
#------------------------------Alternative print way for two decimal points----------------
print(f"you each has to pay " + str(round(finalAmount,2)))
'''

#Alternative method
money = float(input("Enter your Amount: $" ))
interest = int(input("Enter your interest rate 6%, 12% or 18%: "))
friends = int(input("Enter your friends: "))

finalAmount = ((money*(interest/100)+ money)/friends)
print(f"you each has to pay "+ str(round(finalAmount,2)))

#------------------------------Alternative formating problem-------------------

finalAmount = "{:.2f}".format(finalAmount)
print(f"each person should pay: ${finalAmount}")

