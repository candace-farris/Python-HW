# Receive Fahrenheit has an int from user, convert to celsius, and display to one decimal.

print("\nPlease enter your degree in Fahrenheit:\n")

degree = int(input())

def convert (degree):
    celsius = (degree-32)/1.8
    return round(celsius, 1)

print("")
print(degree, "F converts into", convert(degree), "C")

# End of Program
