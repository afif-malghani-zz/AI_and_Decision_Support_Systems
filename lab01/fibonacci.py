# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                        Coded by:                                        #
#                                Muhammad Afif Ul Hasnain                                 #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# get sequence size
print("Enter the number of Numbers to calculate ")
n = int(input(">"))

# get seed values to grow the sequence from
print("Enter seed values")
a = int(input(">"))
b = int(input(">"))

series = [a, b]

# loop to generate new numbers
for i in range(1,n):
    new_num = series[i] + series[i-1]
    series.append(new_num)

# display the results
print("The fibonacci series generated is:")
print(series)