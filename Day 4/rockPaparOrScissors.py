

#Rock paper and scissors.
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''



myChoice = int(input("What do you choose? Type 0 for rock, 1 for paper or 2 for scissors. "))
computerChoose = random.randint(0,2)

if(myChoice >=3 or myChoice < 0):
    print("You Entered invalid number. You lose!")
else:

    myList = [rock,paper,scissors] #These are variables not items or strings.
    choose = myList[myChoice]
    computer = myList[computerChoose]
    
    '''print Statement'''
    print(choose)
    #print(myChoice)
    print(f"computer choose: \n {computer}")
    #print(computerChoose)
    
    
    if(myChoice == computerChoose):
        print("Draw")
    elif(myChoice == 0 and computerChoose == 1 or myChoice == 1 and computerChoose == 2 or myChoice == 2 and computerChoose == 0):
        print("You Loose")
    elif(myChoice == 0 and computerChoose == 2 or myChoice == 1 and computerChoose == 0 or myChoice == 2 and computerChoose == 1):
        print("you win")
    else:
        print("please enter between 0, 1 or 2 you lose!")


    


    











    

