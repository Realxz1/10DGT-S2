# Fence Cost
# Author: Ventresco Sugianto
# 1/11/2024
# Version 1
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


keep_going = ""
while keep_going == "":
    # Get width/height
    width = num_check("Please enter your width: ")
    height = num_check("Please enter your height: ")
    cost = num_check("Cost per meter: ")

    perimeter = 2 * (width + height)

    fence_cost = perimeter * cost

    print()
    print(f"Perimeter: {perimeter} units")
    print(f"Fence Cost: {fence_cost} $")

    keep_going = input("Again? Press <enter> to continue or press any other key to quit")

