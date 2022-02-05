
'''

import random 
from game_data import data
import art

#Random number according to the data
def random_number():
    """Choose a random data form 0 to the length of the data"""
    return random.randint(0, len(data))
    

#Display the Data fetched from data module and give a option to choose.
def random_data(number):
    #print(data[number])
    name = data[number]["name"]
    description = data[number]["description"]
    country = data[number]["country"]
    return name, description, country;
    #print(data[number]["name"])
    #print(data[number]["follower_count"])
    #print(data[number]["description"])
    #print(data[number]["country"])

def followers(number):
    return data[number]["follower_count"]

#if user_answer (Option A/B) is != answer then game ends. Check answer...
#-----------------------------------------------------------------------------
#Sum up the score with each correct answer.



#Check for the user answer (Option A/B). make two variables a and b.

def checking_answer(guess, a_follower, b_follower):
    """Checking who has highest"""
    if a_follower > b_follower:
        return guess == "a"
    elif b_follower > a_follower:
        return guess == "b"
    
    

    

def game():
    """Main game fucntion"""
    score = 0
    game_should_continue = True
    print(art.logo)#-----------------Art logo

    value = random_number()
    #print(value)
    name, description, country = random_data(value)

    a_follower = followers(value)
    print(a_follower)
    print(f"Compare A: {name}, a {description}, from {country}") #---------------------------only value.

    print(art.vs) #--------------------Vs Logo

    value = random_number()
    print(value)
    name, description, country = random_data(value)
    b_follower = followers(value)
    print(b_follower)

    print(f"Against B: {name}, a {description}, from {country}") #--------------------------only value.




    guess = input("Enter your guess")
    #Who have higest follower.
    is_correct = checking_answer(guess, a_follower, b_follower)#---int followers.

    
    
    if is_correct:
        score +=1
        print(f"you're right! current score is {score}")
    else:
        game_should_continue = False
        print(f"Sorry, that's wrong final score is {score}")

    print(f" your final score is {score}")
    

game()









# At the end print the final score.

'''


import random 
from game_data import data
import art

#Random number according to the data
def random_account():
    """Choose a random data form 0 to the length of the data"""
    return random.choice(data)
    

#Display the Data fetched from data module and give a option to choose.

def format_data(account):
  """Format account into printable format: name, description and country"""
  name = account["name"]
  description = account["description"]
  country = account["country"]
  # print(f'{name}: {account["follower_count"]}')
  return f"{name}, a {description}, from {country}"
#--------------------------------------------------------------------
'''def random_data(number):
    #print(data[number])
    name = data[number]["name"]
    description = data[number]["description"]
    country = data[number]["country"]
    return name, description, country;

def followers(number):
    return data[number]["follower_count"]
'''
#if user_answer (Option A/B) is != answer then game ends. Check answer...
#-----------------------------------------------------------------------------
#Sum up the score with each correct answer.



#Check for the user answer (Option A/B). make two variables a and b.

def checking_answer(guess, a_follower, b_follower):
    """Checking who has highest"""
    if a_follower > b_follower:
        return guess == "a"
    elif b_follower > a_follower:
        return guess == "b"
    
    

    

def game():
    """Main game fucntion"""
    score = 0
    game_should_continue = True
    account_a = random_account()
    account_b = random_account()
    print(art.logo)#-----------------Art logo
    while game_should_continue:
        
        account_a = account_b
        #print(value)
        account_b = random_account()

        while account_a == account_b:
            account_b = random_account()

        print(f"Compare A: {format_data(account_a)}")
        print(art.vs)
        print(f"Against B: {format_data(account_b)}")


        guess = input("Enter your guess")
        #-----------------------------------------

        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]

        #---------------------------------------
    
        #Who have higest follower.
        is_correct = checking_answer(guess, a_follower_count, b_follower_count)#---int followers.

        
        
        if is_correct:
            score +=1
            print(f"you're right! current score is {score}")
        else:
            game_should_continue = False
            print(f"Sorry, that's wrong final score is {score}")

        print(f" your final score is {score}")
    

game()









# At the end print the final score.



