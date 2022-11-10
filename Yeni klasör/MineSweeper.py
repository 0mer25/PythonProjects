import random


# Tıkladığımız kısım mayına temas eden bölgelerden birine rastlayana kadar açılması lazım
# Random kısmı çalışmayabiliyor

game = []
showingGame = []
gameOn = True
gameSize = 0
mineNumber = 0

def CreateGame():
    global mineNumber
    global gameSize
    gameSize = input("Enter the size of game (ixi)   i =  ")
    while(True):
        mineNumber = input("Enter the mine number : ")
        if(int(mineNumber) >= (int(gameSize)*int(gameSize))):
            print("You can't enter mine number more than game space (game space = gameSize * gameSize) !!!")
        else:
            break
    
    for i in range(int(gameSize)):
        a = []
        b = []
        for i in range(int(gameSize)):
            a.append("∎")
            b.append(0)
        game.append(b)
        showingGame.append(a)
        
    for i in range(int(mineNumber)):
        x = random.randrange(0 , int(gameSize))
        y = random.randrange(0 , int(gameSize))
        if(game[x][y] == 0):
            game[x][y] = 9
        else:
            i = i - 1
            continue
        
    for i in range(int(gameSize)):
        for j in range(int(gameSize)):
            if(game[i][j] == 0):
                if((i == 0) and (j == 0)):
                    if(game[i + 1][j] == 9):
                        game[i][j] += 1
                    if(game[i][j + 1] == 9):
                        game[i][j] += 1
                elif((i == 0) and (j != 0) and (j != (int(gameSize) - 1))):
                    if(game[i + 1][j] == 9):
                        game[i][j] += 1
                    if(game[i][j + 1] == 9):
                        game[i][j] += 1
                    if(game[i][j - 1] == 9):
                        game[i][j] += 1
                elif((i != 0) and (j == 0) and (i != (int(gameSize) - 1))):
                    if(game[i + 1][j] == 9):
                        game[i][j] += 1
                    if(game[i - 1][j] == 9):
                        game[i][j] += 1
                    if(game[i][j + 1] == 9):
                        game[i][j] += 1
                elif(i == (int(gameSize) - 1)):
                    if(j == 0):
                        if(game[i - 1][j] == 9):
                            game[i][j] += 1
                        if(game[i][j + 1] == 9):
                            game[i][j] += 1
                    elif(j == (int(gameSize) - 1)):
                        if(game[i - 1][j] == 9):
                            game[i][j] += 1
                        if(game[i][j - 1] == 9):
                            game[i][j] += 1
                    else:
                        if(game[i - 1][j] == 9):
                            game[i][j] += 1
                        if(game[i][j - 1] == 9):
                            game[i][j] += 1
                        if(game[i][j + 1] == 9):
                            game[i][j] += 1
                elif(j == (int(gameSize) - 1)):
                    if(i == 0):
                        if(game[i + 1][j] == 9):
                            game[i][j] += 1
                        if(game[i][j - 1] == 9):
                            game[i][j] += 1
                    elif(i == (int(gameSize) -1)):
                        if(game[i - 1][j] == 9):
                            game[i][j] += 1
                        if(game[i][j - 1] == 9):
                            game[i][j] += 1
                    else:
                        if(game[i - 1][j] == 9):
                            game[i][j] += 1
                        if(game[i][j - 1] == 9):
                            game[i][j] += 1
                        if(game[i + 1][j] == 9):
                            game[i][j] += 1
            else:
                continue                 
                        
def ShowGame(x):
    for i in range(len(x)):
        print(x[i])
      
def CheckPosition(x , y , list):
    if(list[int(x)][int(y)] == 9):
        return False    
    else:   
        return True 
    
def PlayGame():
    global mineNumber
    global gameOn
    global gameSize
    remain = (int(gameSize) * int(gameSize)) - int(mineNumber)
    while(gameOn):
        ShowGame(game)
        ShowGame(showingGame)
        
        while(True):
            row = input("Row : ")
            column = input("Column : ") 
            if(((int(row) >= int(gameSize)) or (int(row) < 0)) or ((int(column) >= int(gameSize)) or (int(column) < 0))):
                print("You entered a invalid position !!!")
                continue
            else:
                break
        
        choice = input("1- Empty      2- Flag\n choice : ")
    
        if(choice == "1"):
            if(CheckPosition(row , column , game)):
                showingGame[int(row)][int(column)] = 0
                remain -= 1
                if(remain == 0):
                    print("\nYou Win")
                    ShowGame(game)
                    gameOn = False
                    break
            else:
                print("You Lose")
                ShowGame(game)
                gameOn = False
                break
        elif(choice == "2"):
            showingGame[int(row)][int(column)] = "F"
        elif(choice == "3"):
            gameOn = False
        else:
            print("You entered a invalid number !!!")
    
            
  
CreateGame()
PlayGame()

