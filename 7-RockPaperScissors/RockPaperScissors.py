# Project_7
# Rock-Paper-Scissors

import random

choices = ["rock" , "paper" , "scissors"]

user_point = 0
pc_point = 0



def Check(x , y):
    global user_point,  pc_point
    if(x == "1"):
        if(y == "rock"):
            print("Rock - Rock\n Draw " + str(user_point) + " - " + str(pc_point))
        elif(y == "paper"):
            pc_point += 1
            print("Rock - Paper\n " + str(user_point) + " - " + str(pc_point))
        elif(y == "scissors"):
            user_point += 1
            print("Rock - Scissors\n " + str(user_point) + " - " + str(pc_point))
        else:
            print("You entered a invalid value")
    elif(x == "2"):
        if(y == "rock"):
            user_point += 1
            print("Paper - Rock\n " + str(user_point) + " - " + str(pc_point))
        elif(y == "paper"):
            print("Paper - Paper\n Draw " + str(user_point) + " - " + str(pc_point))
        elif(y == "scissors"):
            pc_point += 1
            print("Paper - Scissors\n " + str(user_point) + " - " + str(pc_point))
        else:
            print("You entered a invalid value")       
    elif(x == "3"):
        if(y == "rock"):
            pc_point += 1
            print("Scissors - Rock\n " + str(user_point) + " - " + str(pc_point))
        elif(y == "paper"):
            user_point += 1
            print("Scissors - Paper\n " + str(user_point) + " - " + str(pc_point))
        elif(y == "scissors"):
            print("Scissors - Scissors\n Draw " + str(user_point) + " - " + str(pc_point))     
        else:
            print("You entered a invalid value")
    else:
            print("You entered a invalid value")                              

while(True):
    pc = random.choice(choices)
    user = input("1-Rock   2-Paper   or   3-Scissors\n Choice : ")
    print(user)
    print(pc)
    Check(user , pc)
    if(user_point == 3):
        print("You Won")
        break
    elif(pc_point == 3):
        print("You Lose")
        break
    else:
        continue
