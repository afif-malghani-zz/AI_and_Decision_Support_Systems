# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                        Coded by:                                        #
#                                Muhammad Afif Ul Hasnain                                 #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


# Import math for tan inv or atan
import math

# Create a class
class compolex():

    # Class constructor
    def __init__(self,a,b):
        self.real = a
        self.imag = b

    # Calculate magnitude
    def magnitude(self):
        magnitude = math.sqrt((self.real) ** 2 + (self.imag) ** 2)
        return magnitude

    # Calculate orientation
    def orientation(self):
        orientation = math.atan(self.imag / self.real)
        return orientation

# get real part from user
print("Enter the real part")
a=int(input(">"))

# get the imaginary part from user
print("Enter the imaginary part : ")
b=int(input(">"))

# create an object of complex number
comp = compolex(a,b)

# Display magnitude
print("Magnitude of the complex number is:")
print(comp.magnitude())

# display Orientation of complex number
print("Orientation of the complex number is:")
print(comp.orientation())