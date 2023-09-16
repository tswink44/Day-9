import os
from art import logo

#Prints logo and intro
print(logo)
print("Welcome to the silent auction program")
#Initializes bid tracker and variable to control repeatability
is_Bidding = True
bidders = {}
while is_Bidding == True:
    #Collects bids
    name = input("What is your name? ")
    bid = input("What is your bid? ")
    bidders[name] = int(bid)
    #If bidding continues, repeat while loop. Else, exit it
    otherbidder = input("Are there any other bidders? 'Yes' if so, otherwise type any other input ")
    if otherbidder == "Yes":
        is_Bidding = True
        os.system('cls')
    else:
        is_Bidding = False
#Initializes variables to determine highest bid
highest_bid = 0
highest_bid_name = ""
#Determines the highest bid and name associated
for key in bidders:
    if bidders[key] > highest_bid:
        highest_bid = bidders[key]
        highest_bid_name = key
#Prints result
print(f"The winner is {highest_bid_name} with a bid of {highest_bid}")


