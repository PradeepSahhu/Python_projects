

#Black_jack/21...


############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.


import random
import art



def deal_card():
    """Returns a random card"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    random_card = random.choice(cards)
    return random_card

def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)
def compare(user_sum, computer_sum):
    if user_sum == computer_sum:
        return "Draw"
    elif computer_sum == 0:
        return "Lose, opponent has Blackjack"
    elif user_sum == 0:
        return "win with a blackjack"
    elif user_sum > 21:
        return "you went over. you lose"
    elif computer_sum > 21:
        return "Opponent went over. You win"
    elif user_sum > computer_sum:
        return "You win"
    else:
        return "you lose"
    
def play_game():
    print(art.logo)
    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:


        user_sum = calculate_score(user_cards)
        computer_sum = calculate_score(computer_cards)

        print(f" your cards: {user_cards} and sum: {user_sum}")
        print(f" computer's first card: {computer_cards[0]}")


            
        if user_sum == 0 or computer_sum == 0 or user_sum > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to ger another card, type 'n' to pass: ").lower()
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_sum != 0 and computer_sum < 17:
        computer_cards.append(deal_card())
        computer_sum = calculate_score(computer_cards)

    print(f" your final hand: {user_cards}, final score: {user_sum}")
    print(f" computer's final hand: {computer_cards}, final score: {computer_sum}")
    print(compare(user_sum, computer_sum))

while input("Do you want to play a game 'y' or 'n'? ").lower() == 'y':
    play_game()
