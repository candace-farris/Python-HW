# Name: Farris, Candace

# Project #: 02

# Project Description:

# Write a program that asks the user to enter the name of his or her favorite city. Store the input and display
# the following information to the console: The number of characters in the city name, the name of the city in all
# uppercase letters, the name of the city in all lowercase letters, the first letter of the city name, and the last
# letter of the city name.
#
# Write a program that computes the tax and tip on a restaurant bill. The program should ask the user to enter
# the charge for the meal. The tax should be 10% of the meal charge. The tip should be 20% of the total after
# adding the tax. Display the meal charge, tax amount, tip amount, and total bill on the console. Dollar values
# should be formatted as $0.00

# Project Filename: Farris_Candace_Project_02

from _decimal import Decimal

print("\n****** PROGRAM 01 ******")

print("\nWhat is your favorite city?\n")

city = input()

print("\nNumber of letters:", len(city))

print("\nUppercase:", city.upper())

print("\nLowercase:", city.lower())

print("\nFirst letter:", city[0])

print("\nLast letter:", city[len(city) - 1])

print("\n\n****** PROGRAM 02 ******\n\n")

print("How much did your meal cost?")

meal = Decimal(input())
tax = Decimal(0.1)
tip = Decimal(0.2)

# Originally tried to set functions to do this, but was having issues with conversions.
# Normal formulas work fine.

getTax = Decimal(meal*tax)  # Tax on meal
totalTax = Decimal(getTax+meal)  # Tax plus the cost of the meal
getTip = Decimal(totalTax*tip)  # Tip of tax+meal
getTotal = Decimal(totalTax+getTip)  # The meal plus tax and tip

# Wasn't quite sure if I used the correct method for formatting, but it works.

print("\nCost of meal:", '${:,.2f}'.format(meal))

print("\nTax amount:", '${:,.2f}'.format(getTax))

print("\nTip amount:", '${:,.2f}'.format(getTip))

print("\nTotal bill:", '${:,.2f}'.format(getTotal))

# End of project
