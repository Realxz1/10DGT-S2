# Conditional statements and while loops
# Author: Ventresco Sugianto
# 2024-09-27
# Version 1
# TODO: Create a program that asks a user ra question and returns a response based on the answer of the user.



# Main loop. keeps running until a condition is met
keep_going = ""
while keep_going == "":
    # Asking the unser for an input to a question
    like_coffee = input("Do you like coffee?").lower()
    
    if like_coffee == "yes" or like_coffee == "y":
        print("I like coffee too")
    elif like_coffee == "no" or like_coffee == "n":
        print("You are missing out!")


        like_tea = input("Would you like tea instead?").upper()
        if like_tea == "YES" or like_tea == "Y":
            print("Good for you. Give coffee another try!")


    else:
         print("I don't understand.")

    keep_going = input("Press <enter> to continue or any key to quit")