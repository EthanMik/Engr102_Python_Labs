# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   *I have not given or received any unauthorized aid on this assignment."
#
# Name:       Ethan Mikolaycik
# Section:    563
# Assignment: Using variables 
# Date:       8/27/2025

from math import *

p = 1
v = 9
L = 0.875
mew = 0.0015
reynolds_num = p*v*L/mew
print("Reynolds number is", reynolds_num)

n = 1
d = .029
theta = 35.0 * pi / 180.0
# Wavelength Equation
wavelength = 2 * d * sin(theta) / n
print("Wavelength is", wavelength, "nm")

q0 = 100.0
Di = 2.0
t = 10.0
b = .8
# Alps Equation
arp = q0 / pow((1.0 + b * Di * t), (1.0 / b))
print("Production rate is", arp, "barrels/day")

v_e = 2029
m_0 = 11000
m_f = 8300
# Rocket Equation
delta_v = v_e*log(m_0/m_f)
print("Change of velocity is", delta_v, "m/s")
