# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   *I have not given or received any unauthorized aid on this assignment."
#
# Name:       Ethan Mikolaycik
# Section:    563
# Assignment: Print Math 
# Date:       8/27/2025

# Calculating gadgets
def gadgets_produced(days):
    if (days < 0 or days > 102):
        print("You entered an invalid number!")
        return
    
    if (days > 100): days = 100

    gadgets = 0
    gadgets_per_day = 10
    
    gadgets = min(days, 10) * gadgets_per_day

    if days > 10: 
        days -= 10
        gadgets += (0.5 * min(days, 40)**2) + (10.5 * min(days, 40))

    if days > 40: 
        days -= 40
        gadgets += (days) * 50

    return gadgets

# days = 99
days = int(input("Please enter a positive value for day: "))
gadgets = gadgets_produced(days)
if (not gadgets == None): print(f"The sum total number of gadgets produced on day {days} is {gadgets:.0f}")