import math
#This file contains all the calculations of EV Chassis

# Let us consider bending stiffness as 4 kN/mm
# For chassis to be safe, it should have bending stiffness >= 3 kN / mm



BendingStiffness=4000 #N/mm
Sb=BendingStiffness


WheelBase=(input("Enter the Wheelbase in mm"))
# WheelBase=2450
l=WheelBase

ModulusofElasticity=float(input("Enter the modulus of elasticity"))
# ModulusofElasticity=200000
E=ModulusofElasticity




MomentofInertia=(Sb*pow(l,3))/(48*E)
print(MomentofInertia)

WidthofOuterRectangleCS=float(input("Width of Outer Rectangle Cross Section"))
#Assumed by trial and error
# WidthofOuterRectangleCS=91
B=WidthofOuterRectangleCS

# WidthofInnerRectangleCS=
WidthofInnerRectangleCS=80
b=WidthofInnerRectangleCS

HeightofOuterRectangleCS=141
H=HeightofOuterRectangleCS

HeightofInnerRectangleCS=130
h=HeightofInnerRectangleCS

I=(B*pow(H,3)/12) - (b*pow(h,3)/12)
print(I)

# Here, I is greater than MomentofInertia, so it satifies the bending stiffness conditon
# Thickness=5.5





