# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   *I have not given or received any unauthorized aid on this assignment."
#
# Name:       Ethan Mikolaycik
# Section:    563
# Assignment: Using variables 
# Date:       8/27/2025

from math import *

print("This program calculates the Reynolds number given velocity, length, and viscosity")
v = float(input("\nPlease enter the velocity (m/s): "))
L = float(input("\nPlease enter the length (m): "))
mew = float(input("\nPlease enter the viscosity (m^2/s): "))
p = 1
reynolds_num = p*v*L/mew
print(f"Reynolds number is {reynolds_num:.0f}")

# Wavelength Equation
print("\nThis program calculates the wavelength given distance and angle")
d = float(input("\nPlease enter the distance (nm): "))
theta = float(input("\nPlease enter the angle (degrees): "))
wavelength = 2 * d * sin(theta * pi / 180.0)

print(f"Wavelength is {wavelength:.4f} nm")
            

# Alps Equation
print("\nThis program calculates the production rate given time, initial rate, and decline rate")
t = float(input("\nPlease enter the time (days): "))
q0 = float(input("\nPlease enter the initial rate (barrels/day): "))
Di = float(input("\nPlease enter the decline rate (1/day): "))
b = .8
arp = q0 / pow((1.0 + b * Di * t), (1.0 / b))
print(f"Production rate is {arp:.2f} barrels/day")

# Rocket Equation
print("\nThis program calculates the change of velocity given initial mass, final mass, and exhaust velocity")
m_0 = float(input("\nPlease enter the initial mass (kg): "))
m_f = float(input("\nPlease enter the final mass (kg): "))
v_e = float(input("\nPlease enter the exhaust velocity (m/s): "))
delta_v = v_e*log(m_0/m_f)
print(f"Change of velocity is {delta_v:.1f} m/s")




