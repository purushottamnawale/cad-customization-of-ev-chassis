
''' For designinig chassis we have to consider bending stiffness(For side members) and torsional stiffness (For cross members)'''
# 1st design for calculating dimensions of side members

import math
Force = 13488.75  # N Force acting on each side member

# in n/mm (For chassis to be safe or avoid bending it should have bending stiffness more than 3 kn/mm)
Bending_Stiffness = 4000

wheelbase = float(input("Enter the wheelbase of vehicle in mm = "))

# Mpa Considering material High carbon steel, typical application for making chassis
Modulus_of_Elasticity = 200000

# Where 'a' is equal to moment of inertia considering Hollow rectangular section
a = Bending_Stiffness*pow(wheelbase, 3)/(48*Modulus_of_Elasticity)

print("Minimum value of moment of inertia to sustain bending load = ", a)

min_lhs = a   # Minimum value for moment of inertia satisfying the value of 'a' so that side members can susutain bending load
max_lhs = 7000000
min_w = 60
max_w = 200
min_t = 4
max_t = 20

# Start with middle values
w = (min_w + max_w) / 2
t = (min_t + max_t) / 2
lhs = ((w * pow(1.5*w, 3))/12) - (((w-2*t)*pow((1.5*w-2*t), 3))/12)

while lhs <= min_lhs or lhs >= max_lhs:
    if lhs <= min_lhs:
        # If lhs is too small, increase w and t
        w += 1
        t += 0.1
    else:
        # If lhs is too large, decrease w and t
        w -= 1
        t -= 0.1
    lhs = ((w * pow(1.5*w, 3))/12) - (((w-2*t)*pow((1.5*w-2*t), 3))/12)

print(f"w = {w:.2f}, t = {t:.2f}")
H = round(1.5*w)
h = round(H-2*t)
W = round(w)
w = round(W-2*t)


print(" Dimensions of rectangular cross section to draw side members ")
print("Width of outer rectangle = ", W, "mm")
print("Width of inner rectangle = ", w, "mm")
print("Height of outer rectangle = ", H, "mm")
print("Height of inner rectangle = ", h, "mm")

# For dimensions of cross members
# We have to consider torsional stiffness with value greater than 4 Kn m/deg for vehical to sustain torsional load
Torsional_Stiffness = 4500000  # n mm/deg

print("For cross member dimensions")

Front_Track = float(input("Enter the front track of vehicle in mm = "))

Length = Front_Track/2

# Torsional force acting on frame (force acting multiplied by perpendicular distance)
Torsional_Force = Force*Length

theta = Torsional_Force/Torsional_Stiffness


tan_theta = math.tan(theta*3.14/180)

x = tan_theta*Length  # Where x is half of the height of cross member

Height_of_the_cross_member = 3*x

Width_of_the_cross_member = Height_of_the_cross_member/1.5
print("Dimensions of cross members")
print("Width of outer rectangle of cross member = ",Width_of_the_cross_member, "mm")
print("Width of inner rectangle of cross member = ",Width_of_the_cross_member-10, "mm")
print("Height of outer cross member = ", Height_of_the_cross_member, "mm")
print("Height of inner cross member = ", Height_of_the_cross_member-10, "mm")
print("length of cross member = ", Front_Track, "mm")
