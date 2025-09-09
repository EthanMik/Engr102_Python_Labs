# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   *I have not given or received any unauthorized aid on this assignment."
#
# Name:       Ethan Mikolaycik
# Section:    563
# Assignment: Print Math 
# Date:       8/27/2025

quarter = 25
dime = 10
nickel = 5
penny = 1

# Calculate change
def calculate_change(cost, paid):
    total_change = int(round((paid - cost) * 100))
        
    num_quarters = total_change // quarter
    quarters_str = "quarters" if num_quarters > 1 else "quarter"
    total_change -= num_quarters * quarter

    num_dimes = total_change // dime
    dimes_str = "dimes" if num_dimes > 1 else "dime"
    total_change -= num_dimes * dime

    num_nickels = total_change // nickel
    nickels_str = "nickels" if num_nickels > 1 else "nickel"
    total_change -= num_nickels * nickel

    num_pennies = total_change // penny
    pennies_str = "pennies" if num_pennies > 1 else "penny"
    total_change -= num_pennies * penny

    return f"{num_quarters} {quarters_str}", f"{num_dimes} {dimes_str}", f"{num_nickels} {nickels_str}", f"{num_pennies} {pennies_str}"

paid = float(input("How much did you pay? "))
cost = float(input("How much did it cost? "))
print(f"You received ${(paid - cost):.2f} in change. That is...")

for item in calculate_change(cost, paid):
    if not item[0] == "0":
        print(item)
