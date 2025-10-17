# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   *I have not given or received any unauthorized aid on this assignment."
#
# Name:       Ethan Mikolaycik
# Section:    563
# Assignment: Print Math 
# Date:       8/27/2025

import math

# clamp bmi into correct band
def bmi_band(bmi: float):
    band = [0, 25, 27.5, 30, 9999999]
    for idx, num in enumerate(band):
        if bmi < num:
            return band[idx - 1]

# Risk table
RISK = {
    "Sex": {"f": 0.879, "m": 0},
    "BMI": {0: 0, 25: 0.699, 27.5: 1.97, 30: 2.518},
    "Hypertension": {"y": 1.222, "n": 0},
    "Steroids": {"y": 2.191, "n": 0},
    "Smoked": {"y": -0.218, "n": 0},
    "Smoker": {"y": 0.855, "n": 0},
    "History": {"y": 0.728, "n": 0},
    "DoubleHistory": {"y": 0.753, "n": 0},
}

# wow user input no way
sex = input("Enter your sex (M/F): ").lower()
age = int(input("Enter your age (years): "))
bmi = float(input("Enter your BMI: "))
hypertension = input("Are you on medication for hypertension (Y/N)? ").lower()
steroids = input("Are you on steroids (Y/N)? ").lower()
smoke_cigarettes = input("Do you smoke cigarettes (Y/N)? ").lower()
used_to_smoke = "n"
if smoke_cigarettes == "n": used_to_smoke = input("Did you used to smoke (Y/N)? ").lower()
# dumbass edge cases wow!!!!
family_history_diabetes = input("Do you have a family history of diabetes (Y/N)? ").lower()
dual_family_history_diabetes = "n"
if family_history_diabetes == "y": 
    dual_family_history_diabetes = input("Both parent and sibling (Y/N)? ").lower()
    if dual_family_history_diabetes == "y": family_history_diabetes = "n"


# math
n = 6.322 + RISK["Sex"][sex] - (0.063 * age) - RISK["BMI"][bmi_band(bmi)] - RISK["Hypertension"][hypertension] - RISK["Steroids"][steroids] - RISK["Smoked"][used_to_smoke] - RISK["Smoker"][smoke_cigarettes] - RISK["History"][family_history_diabetes] - RISK["DoubleHistory"][dual_family_history_diabetes]
risk = 100 / (1 + math.e**n)
print(f"Your risk of developing type-2 diabetes is {risk:.1f}%")

# comment
# comment
# comment
# comment
# comment
# comment
# comment
# comment
# comment
# comment
# comment
# comment
# comment
# comment
# comment
# comment
# comment
# comment
# comment
# comment
# comment
# comment
# comment
# comment
