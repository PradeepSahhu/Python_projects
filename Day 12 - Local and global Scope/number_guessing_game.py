

#Number Guessing Game.

#import random
'''
import art
from random import randint
print(art.logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")


number = randint(1,100)
def lives(level):
    if level == "easy":
        lives = 10
    else:
        lives = 5
    return lives

level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()


lives = lives(level)

game_over = False
while lives > 0 and game_over == False:
    user_guess = int(input("Guess a number: "))

    if user_guess > number:
        lives -=1
        print("too high")
        print("Guess again")
        print(f"you have {lives} attempt left")
    elif user_guess < number:
        lives -=1
        print("too low")
        print("Guess again")
        print(f"you have {lives} attempt left")
    elif user_guess == number:
        print("you won")
        game_over = True
if lives = 0:
    print("You lost")

'''  


#Alternative way...

import art
from random import randint

hard_level = 5
easy_level = 10

#Check the answer of the user.
def check_answer(user_guess, number, turns):
    
    if user_guess > number:
        print("too high")
        return turns - 1
    elif user_guess < number:
        print("too low")
        return turns - 1
    else:
        print(f"you got it! The answer was {number}")

def lives():
    """ level of the user based on his input"""
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if level == "easy":
        return easy_level
    else:
        return hard_level
    



def game(): 
    print(art.logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    number = randint(1,100)

    
    turns = lives()
    user_guess = 0
    while user_guess != number:
        print(f"you have {turns} attempt left")
        
        user_guess = int(input("Guess a number: "))
        
        
        turns = check_answer(user_guess, number, turns)

        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif user_guess != number:
            print("Guess again")
            

game()

'''
from random import randint
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

#Function to check user's guess against actual answer.
def check_answer(guess, answer, turns):
  """checks answer against guess. Returns the number of turns remaining."""
  if guess > answer:
    print("Too high.")
    return turns - 1
  elif guess < answer:
    print("Too low.")
    return turns - 1
  else:
    print(f"You got it! The answer was {answer}.")

#Make function to set difficulty.
def set_difficulty():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level == "easy":
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS

def game():
  print(logo)
  #Choosing a random number between 1 and 100.
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  answer = randint(1, 100)
  print(f"Pssst, the correct answer is {answer}") 

  turns = set_difficulty()
  #Repeat the guessing functionality if they get it wrong.
  guess = 0
  while guess != answer:
    print(f"You have {turns} attempts remaining to guess the number.")

    #Let the user guess a number.
    guess = int(input("Make a guess: "))

    #Track the number of turns and reduce by 1 if they get it wrong.
    turns = check_answer(guess, answer, turns)
    if turns == 0:
      print("You've run out of guesses, you lose.")
      return
    elif guess != answer:
      print("Guess again.")


game()
'''
    
