# Project_8
# Hangman

import random

wordsss = ["harry potter" , "prison break" , "breaking bad" , "the gravity" , "fight club"]

live = 5
sameLetter = False
guessed = False
gameOver = False
wordHasGuessed = False
letterNumber = 0
guesses = [""]

word = random.choice(wordsss)      # Choose a word randomly
letterNumber = len(word) - 1

answer = list(word)                # Get the every character of the word


game = ["_"] * len(answer)


for i in range(len(answer)):       # Set the empty chars
    if(answer[i] == " "):
        game[i] = " "

while(gameOver == False):
    
    print("  live : " + str(live))  
    for i in game:                     
        print(i , end = "  ")
            
    guess = input("\n guess : ")             # Get input
    
    
    for i in range(0 , (len(guesses) + 1)): 
        if(i != 0):
            if(guesses[i - 1] == guess):
                print("\nYou already said that letter")
                print("\n")
                sameLetter = True
                break
            else:
                continue
        else:
            continue
    
    if(sameLetter):
        sameLetter = False
        continue
    else:
        guesses.append(guess)    
        sameLetter = False
    
     
     
    
    print("\t\t\t\t\t\t  your guesses : " + str(guesses))         # Show the letters that user enter
    
    if(guess == "0"):
        print("GameOver")
        break
    
    

    for i in range(0 , len(answer)):          # Check if the user guessed and if user did print that letter in the game
        if(answer[i] == guess):
            game[i] = guess
            letterNumber -= 1
            if(letterNumber == 0):
                wordHasGuessed = True
            guessed = True
        else:
            if(guessed):
                continue
            else:
                guessed = False
       
        if(wordHasGuessed):
            break   
    
    
    if(wordHasGuessed):
        break            
        

    if(guessed == False):             # if user make a wrong guess , reduce live by 1
        live -= 1
        guessed = True
        if(live == 0):
            break
    
    guessed = False                 
    
    
    

if((live == 0) or wordHasGuessed):        # End of the game       
        gameOver = True
        if(live == 0):
            print("  You Lose")
            print("Movie's name was -> " + word)
        else:
            print("  You Won")    

