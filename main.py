# Our Blackjack Game House Rules
# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The Ace can count as 11 or 1.
# Use the following list as the deck of cards:
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.
import random

gameOn = True

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]        #creating the needed lists
computer = []
user = []

def deal_cards():                                           #function to deal cards
    computer.append(random.choice(cards)) 
    computer.append(random.choice(cards)) 
    user.append(random.choice(cards)) 
    user.append(random.choice(cards)) 

deal_cards()                                            #calling function to deal the cards

computer_score = sum(computer)                          #summing the scores of the computer and user
user_score = sum(user)

if computer_score == 21:                                #if statements to see if either the computer or user got a blackjack then ending the game if they did
    print("The computer got a blackjack! You lose!")
    gameOn = False
elif user_score == 21:
    print("You got a blackjack! You win!")
    gameOn = False

print(f"Your cards: {user}, current score: {user_score}")       #showing user their cards and current score
print(f"Computer's first card : {computer[0]}")                 #showing computer's first card