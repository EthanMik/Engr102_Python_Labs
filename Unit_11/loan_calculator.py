# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   *I have not given or received any unauthorized aid on this assignment."
#
# Name:       Ethan Mikolaycik
# Section:    563
# Assignment: Print Math 
# Date:       8/27/2025

# create monthly payment
def monthly_payment(P: float, i: float, N: float):
    format = ""
    balance = P
    interest = 0
    total_interest = 0

    format += "Month,Total Accrued Interest,Loan Balance\n"
    format += f"0,${interest:.2f},${balance:.2f}\n"

    M = (balance * i / 12) / (1 - (1 / (1 + i / 12)) ** N)
    for n in range(1, N + 1):

        interest = balance * (i / 12)
        balance += interest - M
        total_interest += interest

        balance = max(0, balance)
        line = f"{n},${total_interest:.2f},${balance:.2f}"

        if n < N:
            format += line + "\n"
        else: format += line

    return format

output_path = input("Enter the output filename: ")
P = float(input("Enter the principal amount: "))
N = int(input("Enter the term length (months): "))
I = float(input("Enter the annual interest rate: "))
s = monthly_payment(P, I, N) 
# s = monthly_payment(100_000, .025, 60) 

with open(output_path, "w") as f:
    f.write(s)


