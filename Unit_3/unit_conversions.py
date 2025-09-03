# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   *I have not given or received any unauthorized aid on this assignment."
#
# Name:       Ethan Mikolaycik
# Section:    563
# Assignment: Print Math 
# Date:       8/27/2025

units = float(input())

newtons = units * 4.4482221

feet = units * 3.280839895
kilopascals = units * 101.325
BTUhour = units * 3.412141633
gallons = units * 15.850323140625
fahrenheit = (units * 1.8) + 32

# Print all conversions
print(f"Please enter the quantity to be converted:")
print(f"{units:.2f} pounds force is equivalent to {newtons:.2f} newtons")
print(f"{units:.2f} meters is equivalent to {feet:.2f} feet")
print(f"{units:.2f} atmospheres is equivalent to {kilopascals:.2f} kilopascals")
print(f"{units:.2f} watts is equivalent to {BTUhour:.2f} BTU per hour")
print(f"{units:.2f} liters per second is equivalent to {gallons:.2f} US gallons per minute")
print(f"{units:.2f} degrees Celsius is equivalent to {fahrenheit:.2f} degrees Fahrenheit")
