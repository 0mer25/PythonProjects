# Project_9
# Password Generator

import random

vowels = ["a" , "e" , "i" , "u" , "o"]
consonants = ["b" , "d" , "f" , "h" , "k" , "l" , "m" , "n" , "p" , "s" , "t" , "v" , "w" , "z" , "g" , "j"]
numbers = ["1" , "2" , "3" , "4" , "5" , "6" , "7" , "8" , "9" , "0"]
symbols = ["~" , "`" , "!" , "@" , "#" , "$" , "%" , "^" , "&" , "*" , "(" , ")" , "_" , "-" , "+" , "=" , "{" , "[" , "}" , "]" , "|" ,
":" , ";" , "'" , "<" , ">" , "." , "?" , "/"]

all = vowels + consonants + numbers + symbols

generatedPass = []
tempList = []

digitNumber = input("Enter the digit number of password : ")

choice = input("1-Mix all the characters   or   2-Choose the number of characters : ")

while(True):
    if(choice == "1"):
        for i in range(0 , int(digitNumber)):
            generatedPass.append(random.choice(all))
        break    
    elif(choice == "2"):
        temp = input("Vowel number : ")
        for i in range(0 , int(temp)):
            generatedPass.append(random.choice(vowels))
        
        temp = input("Consonant number : ")
        for i in range(0 , int(temp)):
            generatedPass.append(random.choice(consonants))
        
        temp = input("Symbol number : ")
        for i in range(0 , int(temp)):
            generatedPass.append(random.choice(symbols))
        
        temp = input("Number number : ")
        for i in range(0 , int(temp)):
            generatedPass.append(random.choice(numbers))
        break
    else:
        choice = input("Please enter a valid digit number : ")        


for i in range(len(generatedPass)):
    print(generatedPass[i] , sep = None , end = "")

