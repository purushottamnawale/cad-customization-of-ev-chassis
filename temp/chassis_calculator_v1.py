import math
import unknown_finder # imported a custom module


# This file contains all the calculations of EV Chassis

# Let us consider bending stiffness as 4 kN/mm
# For chassis to be safe, it should have bending stiffness >= 3 kN / mm


BendingStiffness = 4000  # N/mm
Sb = BendingStiffness


# WheelBase=(input("Enter the Wheelbase in mm"))
WheelBase = 2450
l = WheelBase

# ModulusofElasticity=float(input("Enter the modulus of elasticity"))
ModulusofElasticity = 200000
E = ModulusofElasticity


MomentofInertia = (Sb*pow(l, 3))/(48*E)
print(MomentofInertia)

# WidthofOuterRectangleCS=float(input("Width of Outer Rectangle Cross Section"))
# Assumed by trial and error
W = WidthofOuterRectangleCS = unknown_finder.W
w = WidthofInnerRectangleCS = unknown_finder.w
H = HeightofOuterRectangleCS = unknown_finder.H
h = HeightofInnerRectangleCS = unknown_finder.h
I = (W*pow(H, 3)/12) - (w*pow(h, 3)/12)
print(I)

# Here, I is greater than MomentofInertia, so it satifies the bending stiffness conditon
# Thickness=5.5
