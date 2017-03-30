# Name: Farris, Candace

# Project #: 01

# Project Description:
# "Your company, QuickFence, Inc. builds fences and installs sod for residential yards. You have been asked to
# write a program that will calculate the perimeter and area of a fenced yard. A customer should be able to enter
# the yard's width and length. The charge to install fencing is $5 per foot. The charge to install sod is $3 per
# square foot. Display the yard's perimeter, area, and install price for the fence and sod.

# Project Filename: Farris_Candace_Project_01

######################

# Issue prompt for user

print("\nHello. Please enter the length and width of your yard.\n")

# Declare and assign variables

length = input("Length: ")
width = input("Width: ")
fencing = 5
sod = 3

# Create functions

# Note: type-cast strings into ints

def Perimeter(width, length):
    perimeter = (int(width) * 2) + (int(length) * 2)
    return perimeter


def Area(width, length):
    area = int(width) * int(length)
    return area


def fenceCost():
    cost = fencing * Perimeter(width, length)
    return cost


def sodCost():
    cost = sod * Area(width, length)
    return cost


print("\nThe perimeter of your yard is: ", Perimeter(width, length))
print("\nThe area of your yard is: ", Area(width, length))
print("\nThe cost of fencing would be: $", fenceCost())
print("\nThe cost of sod would be: $", sodCost())
print("\nTotal Cost: $", (fenceCost()+sodCost()))

# End of program
