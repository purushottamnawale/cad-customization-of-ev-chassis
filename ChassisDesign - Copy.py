import math

Weight = 2000
Force = (2000+500)*9.81
Force_on_each_side_member = Force/2 

Bending_Stiffness = 4000
wheelBase = float(input("Enter the wheelbase of vehicle in mm = ") or "2450")

Modulus_of_Elasticity = 200000

a = Bending_Stiffness*pow(wheelBase, 3)/(48*Modulus_of_Elasticity)
print("Minimum value of moment of inertia to sustain bending load = ", a)

def trialAndError():
    global W, w, H, h
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


Torsional_Stiffness = 4500000
print("For cross member dimensions")
Front_Track = float(input("Enter the front track of vehicle in mm = ") or "1520")
Length = Front_Track/2

Torsional_Force = Force_on_each_side_member*Length
theta = Torsional_Force/Torsional_Stiffness

tan_theta = math.tan(theta*3.14/180)
x = tan_theta*Length
Height_of_the_cross_member = 3*x

Width_of_the_cross_member = Height_of_the_cross_member/1.5
print("Dimensions of cross members")
print("Width of outer rectangle of cross member = ",Width_of_the_cross_member, "mm")
print("Width of inner rectangle of cross member = ",Width_of_the_cross_member-10, "mm")
print("Height of outer cross member = ", Height_of_the_cross_member, "mm")
print("Height of inner cross member = ", Height_of_the_cross_member-10, "mm")
print("length of cross member = ", Front_Track-2*W, "mm")