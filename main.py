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


while gameOn:
    def calculate_blackjack():                                  #put all the calculation operations into a function so it can be easily called

        if computer_score == 21:                                #if statements to see if either the computer or user got a blackjack then ending the game if they did
            print("The computer got a blackjack! You lose!")
            gameOn = False
        elif user_score == 21:
            print("You got a blackjack! You win!")
            gameOn = False

        print(f"Your cards: {user}, current score: {user_score}")       #showing user their cards and current score
        print(f"Computer's first card : {computer[0]}")                 #showing computer's first card

        if user_score > 21:                                              #if statement to check if user has a score above 21
            for card in user:
                if card == 11:                                          #checking to see if user has been dealt an ace and then seeing if they would lose if the ace became 1
                    if user_score - 10 > 21:
                        print("You got higher than 21. You lose!")
                        gameOn = False
                else:                                                    #if no ace then they automatically lose
                    print("You got higher than 21. You lose!")
                    gameOn = False
    calculate_blackjack()

    take_another = input("Type 'y' to get another card, type 'n' to pass: ")

    if take_another == "y":                                 #if statement to check if user wants to pull another card
        user.append(random.choice(cards))                   #if yes then add a new card to their list                  
        user_score = sum(user)                                #re calculate user score
        calculate_blackjack()                               #put it back through calculation function


    if computer_score < 17:                                 #if computer score is less than 17, then pull new card
        computer.append(random.choice(cards))
        computer_score = sum(computer)                      #sum up computer score
        calculate_blackjack()                               #put through calculation function

    if computer_score > 21:                                 #if computer score is greater than 21, user wins
        print("The computer has gone over 21. You win!")
        gameOn = False

    if user_score > computer_score:
        print("You got closer to 21. You win!")
    elif computer_score > user_score:
        print("The computer got closer to 21. You lose!")
    else:
        print("It's a draw!")

    gameOn = False