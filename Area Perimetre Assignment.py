# Complete Area Perimetre Assignment
# Author: Ventresco Sugianto
# 30/10/2024
# Version 1
# Copied number checker from past task
def num_check(question):

    
    error = "Please enter a number that is more than zero\n"
    while True:

        try:
            response = float(input(question))

            if response > 0:
                return response
            else:
                print(error)

        except ValueError:
            print(error)

# Main routine goes here...

keep_going = ""
while keep_going == "":
    # Get width and height

    width = num_check("Please enter your width: ")
    height = num_check("Please enter your height: ")
    
    # Calculate Area/Perimetre
    area = width * height
    perimetre = 2 * (width + height)

    # Display output
    print(f"Perimetre: {perimetre} units")
    print(f"Area: {area} units")

    # Ask user if they want to keep going
    keep_going = input("Again? Press <enter> to continue or press any other key to quit")
