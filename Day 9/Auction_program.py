
#Auction program.
import logo
#import clear
print(logo.logo)
dictionary = {}


def heighest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if(bid_amount > highest_bid):
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")
    
        
    

    
    
is_continue = True
while is_continue:    #means choose == True
    name = input("Enter your name: ")
    money = int(input("Enter your bid $"))
    dictionary[name] = money
    choose = input("Is there anyone left to bid? yes/no \n").lower()
    if choose == "yes":
        is_continue = True
    else:
        is_continue = False
        heighest_bidder(dictionary)
 

