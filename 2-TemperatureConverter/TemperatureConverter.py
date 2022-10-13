# Project_3
# Temperature Converter


choice1 = input("Choose the type of first temperature\n 1- Celcius   2- Fahrenheit   3- Kelvin\n choice : ")
tempValue = input("Enter the temperature : ")

choice2 = input("Choose the type of first temperature\n 1- Celcius   2- Fahrenheit   3- Kelvin\n choice : ")

if(choice1 == "1"):
    if(choice2 == "1"):
        print("Did you just tried to convert C to C ¯\_( ͡❛ ͜ʖ ͡❛)_/¯")
    elif(choice2 == "2"):
        print(tempValue + " C = " + str((float(tempValue) * (9/5)) + 32) + " F")
    elif(choice2 == "3"):
        print(tempValue + " C = " + str(float(tempValue) + 273.15) + " K")
    else:
        print("You entered a invalid value") 
elif(choice1 == "2"):
    if(choice2 == "1"):
        print(tempValue + " F = " + str((float(tempValue) - 32) * (5/9)) + " C")
    elif(choice2 == "2"):
        print("Did you just tried to convert F to F ¯\_( ͡❛ ͜ʖ ͡❛)_/¯")
    elif(choice2 == "3"):
        print(tempValue + " F = " + str((float(tempValue) - 32) * (5/9) + 273.15) + " K")
    else:
        print("You entered a invalid value")   
elif(choice1 == "3"):
    if(choice2 == "1"):
        print(tempValue + " K = " + str((float(tempValue) - 273.15)) + " C")
    elif(choice2 == "2"):
        print(tempValue + " K = " + str(((float(tempValue) - 273.15) * (9/5)) + 32) + " F")
    elif(choice2 == "3"):
        print("Did you just tried to convert K to K ¯\_( ͡❛ ͜ʖ ͡❛)_/¯")
    else:
        print("You entered a invalid value")
else:
        print("You entered a invalid value")
