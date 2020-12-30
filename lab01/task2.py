# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                        Coded by:                                        #
#                                Muhammad Afif Ul Hasnain                                 #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# define function
def fact(n):
    # if n is greater than 0, take fact of n-1
    if n > 0:
        return n*fact(n-1)
    # if n <= 0, return 1
    else:
        return 1

# ask the user to input a number
print("Enter the number you want the factorial to be calculated for")

# got the input
cin = int(input(">"))

# calculate factorial
factorail = fact(cin)

# display
print(str(cin)+"! = "+str(factorail))