

choice = input("1-Password to Encryption     or    2-Encryption to Password\n Choice : ")

if(choice == "1"):
    password = input("Enter your password : ")

    lengthOfPass = len(password)

    listOfPassChars = range(lengthOfPass)  # create a list with elements of the same length as the password

    new_list = [ord(password[x]) for x in listOfPassChars]    # get ASCII values for characters

    new_list = [x+1 for x in new_list]   # add 1 to every ASCII value of the characters

    new_list = [chr(x) for x in new_list]
    
    new_pass = ""
    for x in new_list:
        new_pass = new_pass + str(x)
    
    print("new password : " + new_pass)        

elif(choice == "2"):
    password = input("Enter your password : ")

    lengthOfPass = len(password)

    listOfPassChars = range(lengthOfPass)  # create a list with elements of the same length as the password

    new_list = [ord(password[x]) for x in listOfPassChars]    # get ASCII values for characters

    new_list = [x-1 for x in new_list]   # add 1 to every ASCII value of the characters

    new_list = [chr(x) for x in new_list]
    
    new_pass = ""
    for x in new_list:
        new_pass = new_pass + str(x)
    
    print("new password : " + new_pass) 

else:
    print("You entered a invalid value")