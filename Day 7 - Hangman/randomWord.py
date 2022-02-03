#Step 1 

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

import random

#Asking the user to Guess a word.
user_guess = input("Guess a Letter: ").lower()

#Generating the random word
'''randNum = random.randint(0, len(word_list)-1)
rand_word = word_list[randNum]
'''
#Alternative of the above.
rand_word = random.choice(word_list)



#Slicing the random word using for loop.
for char in rand_word:
    if(char == user_guess):
        print("True")
    else:
        print("False")

'''for debugging use Thonny '''
