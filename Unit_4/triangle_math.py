# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   *I have not given or received any unauthorized aid on this assignment."
#
# Name:       Ethan Mikolaycik
# Section:    563
# Assignment: Print Math 
# Date:       8/27/2025

def proper_lengths(hyp: float, opp: float, adj: float) -> bool:
    return opp**2 + adj**2 == hyp**2

# Calculates triangle
def calculate_triangle(hyp: float, opp: float, adj: float, operation: int) -> float:
    TRIG = {
        1: ["sin(θ)", opp / hyp],
        2: ["cos(θ)", adj / hyp],
        3: ["tan(θ)", opp / adj],
        4: ["csc(θ)", 1 / (opp / hyp)],
        5: ["sec(θ)", 1 / (adj / hyp)],
        6: ["cot(θ)", 1 / (opp / adj)],
    }

    return TRIG[operation]

def main():
    hyp = float(input("Enter the hypotenuse: "))
    opp = float(input("Enter the opposite side: "))
    adj = float(input("Enter the adjacent side: "))

    if not proper_lengths(hyp, opp, adj):
        print("Those lengths don't form a right triangle!")
        return

    print("What would you like to calculate?")
    operation = int(input("1: sin(θ), 2: cos(θ), 3: tan(θ), 4: csc(θ), 5: sec(θ), 6: cot(θ): "))
    output = calculate_triangle(hyp, opp, adj, operation)
    print(f"For a right triangle of sides {opp:.1f}, {adj:.1f}, and {hyp:.1f}, {output[0]} = {output[1]:.1f}")

main()