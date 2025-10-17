# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   *I have not given or received any unauthorized aid on this assignment."
#
# Name:       Ethan Mikolaycik
# Section:    563
# Assignment: Print Math 
# Date:       8/27/2025

# find range
def clamp_to_band(band: list, value: float) -> list:
    for idx, item in enumerate(band):
        if value < item:
            if idx == 0: return [item]
            return [band[idx - 1], item]
  
def percent_error(nominal: float, actual: float):
    return abs(1 - actual / nominal) * 100

nom = float(input(f"Enter the nominal diameter: "))
act = float(input("Enter the actual diameter: "))
band = clamp_to_band([1, 2, 5], percent_error(nom, act))
if band is None:
    print("Out of specifications, >=5% error")
elif len(band) > 1:
    print(f"The diameter is between {band[0]}% and <{band[1]}% of desired value")
else: 
    print(f"The diameter is within <{band[0]}% of desired value")
