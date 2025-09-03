# user_input = input()
units = float(input())

newtons = units * 4.4482221

feet = units * 3.280839895
kilopascals = units * 101.325
BTUhour = units * 3.412141633
gallons = units * 3.785411784
fahrenheit = (units * 1.8) + 32

print(f"Please enter the quantity to be converted: {units:.2f}")
print(f"{units:.2f} pounds force is equivalent to {newtons:.2f} newtons")
print(f"{units:.2f} meters is equivalent to {feet:.2f} feet")
print(f"{units:.2f} atmospheres is equivalent to {kilopascals:.2f} kilopascals")
print(f"{units:.2f} watts is equivalent to {BTUhour:.2f} BTU per hour")
print(f"{units:.2f} liters per second is equivalent to {gallons:.2f} US gallons per minute")
print(f"{units:.2f} degrees Celsius is equivalent to {fahrenheit:.2f} degrees Fahrenheit")
