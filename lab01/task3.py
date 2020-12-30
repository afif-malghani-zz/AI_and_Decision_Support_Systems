# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                        Coded by:                                        #
#                                Muhammad Afif Ul Hasnain                                 #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Get initial string as input
print("Enter a string")
strin = input(">")

# split the string
strin = strin.split(" ")

# declare empty string
piglatin = ""

# loop through splitted string parts
for substr in strin:

    # if full stop or comma or exclaimation mark or question mark, skip
    if substr[-1] == '.' or substr[-1] == ',' or substr[-1] == '!' or substr[-1] == '?':
        temp = substr[0]

        # use second to last character and not the last character
        temp1 = substr[-2]
        piglatin = piglatin + temp1 + substr[1:-2] + temp + substr[-1] +" "

    else:
        temp = substr[0]
        temp1 = substr[-1]
        piglatin = piglatin + temp1 + substr[1:-1] + temp + " "

# print oputput
print(piglatin)