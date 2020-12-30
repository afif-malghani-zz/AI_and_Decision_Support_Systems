# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                        Coded by:                                        #
#                                Muhammad Afif Ul Hasnain                                 #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Import OS to clear python shell
import os

# Import time for sleep(). otherwise, shell clears instantly
import time

# Addition Function
def add(a, b):
    return a+b

# subtraction Function
def sub(a, b):
    return a-b

# Multiplication Function
def mul(a, b):
    return a*b


# division Function
def div(a, b):
    return a/b

# display menu Function
def menu():
    while True:
        # wait 3 seconds
        time.sleep(3)

        # Clear shell
        os.system('clear')

        # Print the menu out
        print("Please choose one of the following options to proceed")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("9. Exit")

        # get user input
        inp = int(input(">"))

        # If user chooses to exit
        if(inp == 9):
            break

        # Else if user chooses to add 2 numbers
        elif (inp == 1):
            print("Enter the first number")
            a = int(input(">"))
            print("Enter the second number")
            b= int(input(">"))
            sum = add(a, b)

            print(str(a) +' + ' + str(b) + ' = ' + str(sum))

        # Else if user chooses to subtract one number from another
        elif (inp == 2):
            print("Enter the first number")
            a = int(input(">"))
            print("Enter the second number")
            b = int(input(">"))
            diff = sub(a, b)

            print(str(a) + ' - ' + str(b) + ' = ' + str(diff))


        # Else if user chooses to multiply 2 numbers
        elif (inp == 3):
            print("Enter the first number")
            a = int(input(">"))
            print("Enter the second number")
            b = int(input(">"))
            prod = mul(a, b)

            print(str(a) + ' * ' + str(b) + ' = ' + str(prod))

        # Else if user shooses to divide one number over the other
        elif (inp == 4):
            print("Enter the first number")
            a = int(input(">"))
            print("Enter the second number")
            b = int(input(">"))
            quot = div(a, b)

            print(str(a) + ' / ' + str(b) + ' = ' + str(quot))

        # If user input is not any expected value:
        else:
            print("Invalid selection!")
            continue

# Funcrtion call for menu display.
menu()