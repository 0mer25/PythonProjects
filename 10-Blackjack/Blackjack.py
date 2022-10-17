# Project_10
# Blackjack - 21

import random

x = True

def DisplayGame():
    global x
    if(x):
        print("Your Cards : " + str(userCards) + "\t\t\t You : " + str(Check(userCards)))
        print("Opponent's Cards : " + str(opponentCards[0]) + " , ?" + "\t\t\t Opponent : " + str(opponentCards[0]) + " + ?")
    else:
        print("Your Cards : " + str(userCards) + "\t\t\t You : " + str(Check(userCards)))
        print("Opponent's Cards : " + str(opponentCards)+ "\t\t\t Opponent : " + str(Check(opponentCards)))
     
    

def TakeCard():
    y = random.choice(cards)
    for i in range(len(cards)):
        if(cards[i] == y):
            cards.remove(y)
            break
    return y

def Check(y):
    userSum = 0
    for i in y:
        userSum += i
    return userSum    

def Game():
    global x
    
    userCards.append(TakeCard())
    userCards.append(TakeCard())
        
    opponentCards.append(TakeCard())
    opponentCards.append(TakeCard())
        
    while(True):
        DisplayGame()
        choice = input("<i>n  or  <o>ut :  ")
        if(choice == "i"):
            userCards.append(TakeCard())
            if(Check(userCards) == 21):
                x = False
                DisplayGame()
                print("You Won")
                break
        elif(choice == "o"):
            x = False
            while(True):
                if(Check(opponentCards) < 22):
                    opponentCards.append(TakeCard())
                    # DisplayGame()
                    if(Check(opponentCards) > 21):
                        opponentCards.reverse()
                        opponentCards[0] = 0
                        DisplayGame()
                        if(Check(userCards) > Check(opponentCards)):
                            print("You Won")
                            break
                        elif(Check(userCards) == Check(opponentCards)):
                            print("Draw")
                            break
                        else:
                            print("You Lose")
                            break
                    else:
                        continue

            break
        else:
            print("Enter e valid value")
            continue
        
        if(Check(userCards) > 21):
            x = False
            DisplayGame()
            print("You Lose")
            break
        else:
            continue
            
userCards = []
opponentCards = []
    
a = [1,2,3,4,5,6,7,8,9,10,10,10,10]
b = [1,2,3,4,5,6,7,8,9,10,10,10,10]
c = [1,2,3,4,5,6,7,8,9,10,10,10,10]
d = [1,2,3,4,5,6,7,8,9,10,10,10,10]

cards = a + b + c + d

Game()

