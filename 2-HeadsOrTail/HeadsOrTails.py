# Project_2
# HeadsOrTails

import random

user = input("1-Heads or 2-Tails : ")
pc = random.randrange(1,3)
print(pc)

while(True):
    if(user == "1"):
        if(pc == 1):
            print("You Win")
        else:
            print("You Lose")
        break
    elif(user == "2"):
        if(pc == 1):
            print("You Lose")
        else:
            print("You Win")
        break
    else:
        print("Please enter a valid value")
        


