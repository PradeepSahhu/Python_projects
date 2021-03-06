#Step 2

import random
word_list = ["aardvark", "baboon", "camel"]
empty_list = []
chosen_word = random.choice(word_list)

#Testing code
print(f'cheating, the solution is {chosen_word}.')

#TODO-1: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.

guess = input("Guess a letter: ").lower()

#TODO-2: - Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].
'''
num = 0
for letter in chosen_word:
    empty_list.append("_")

    #Alternative.
    empty_list += "_"

    if letter == guess:
        empty_list[num] = letter
    num+=1
    
print(empty_list)

'''
#TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".

#Alternative way.
word_count = len(chosen_word)
for _ in chosen_word:
    empty_list += "_"

for position in range(0, word_count):
    letter = chosen_word[position]
    if letter == guess:
        empty_list[position] = letter

print(empty_list)




#Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.
