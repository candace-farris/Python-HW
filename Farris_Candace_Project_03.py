# Name: Farris, Candace

# Project #: 03

# Project Description:
# Write a program that lets the user enter six (6) values into a list. The program should calculate and display
# the sum, the average, the highest and the lowest values of all the numbers entered.

# Project Filename: Farris_Candace_Project_03

print("\nPlease input 6 numbers:\n")


nums = [int(x) for x in input().split()[:6]]  # Input 6 digits only

print("")
print(nums)

print("\nSum:", sum(nums))
print("\nAverage:", sum(nums)/len(nums))
print("\nHighest number:", max(nums))
print("\nLowest number:", min(nums))

# End of program
