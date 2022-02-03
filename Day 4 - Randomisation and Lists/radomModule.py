#random module

'''import random
randomInteger = random.randint(0,5)
print(randomInteger)

randomFloat = random.random()*5
print(randomFloat)
'''

#Heads or tails: 0 means tails and 1 means Heads.
'''
import random
randomSide = random.randint(0,1)
if(randomSide == 1):
    print("Heads")
else:
    print("Tails")
'''
#List appending and extending...
'''name = ["Delhi","U.P","Rajasthan","J&K","Bihar","Jharkhand","Maharastra"]
name.extend(["Goa","Arunachal Pradesh","Kerela"])
print(name)
'''
#Program... of paying bill by random person...
'''import random
card = ["pradeep sahu","Ritik sahu","Sumit sahu","Sandeep sahu","Roshan sahu"]
random_name = card[random.randint(0,len(card)-1)]
print(f"{random_name} is going to buy the meal.")
'''
#split string method... important!!!
'''name_string = input("Give me everybody's names ")
name = name_string.split(", ")
print(name)
'''
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
 
dirty_dozen = [fruits, vegetables]
 
print(dirty_dozen[1][1])
                   
                   
