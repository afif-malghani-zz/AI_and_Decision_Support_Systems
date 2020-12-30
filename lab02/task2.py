# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                        Coded by:                                        #
#                                Muhammad Afif Ul Hasnain                                 #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


# import numpy for arrays and math for mathematical operations
import numpy as np
import math

# given discrete sequence
x = [2, 2, 2, 2, 2, 2, 2, 2, 2]
length= len(x)

# get size of numpy array
size = np.size(x)

# crerate an array of complex numbers, same size
comp = np.zeros((size,), dtype=np.complex128)

# Iterate
for m in range(0, size):
    for n in range(0, size):

        comp[m] += x[n] * np.exp(-np.pi * 2j * m * n / size)
print(comp)

# create a class for complex numbers
class Complex():

    # class constructor
    def __init__(self,a,b):
        self.real = a
        self.imag = b
    # calculate magnitude
    def magnitude(self):
        magnitude = math.sqrt((self.real) ** 2 + (self.imag) ** 2)
        return magnitude

    # Get orientation
    def orientation(self):
        orientation = math.atan(self.imag / self.real)
        return orientation

# inherited class
class inherited(Complex):
    def __init__(self,a,b):
        super().__init__(a,b)

# iterate
for i in range(len(comp + 1)):

    print("Magnitude and Phase spectra of " + str(i+1) + "number is :")

    # get real and imaginary parts of the complex number
    a=comp[i].real
    b=comp[i].imag

    output=inherited(a,b)

    # calculate and display magnitude
    print("magnitude:")
    print(output.magnitude())

    # calaculate and display phase sepctrum
    print("Phase spectrum:")
    print(output.orientation())