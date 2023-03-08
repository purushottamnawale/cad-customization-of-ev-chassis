# Given equation
eqn = lambda B, b, H, h: (B*pow(H,3)/12) - (b*pow(h,3)/12)

# Constants
MIN_B = 50
MAX_B = 150
MIN_b = 45
MAX_b = 140
MIN_H = 80
MAX_H = 200
MIN_h = 75
MAX_h = 190
TARGET = 6127552.083333333
MAX_ITERATIONS = 1000

# Starting values
B = (MIN_B + MAX_B) // 2
b = (MIN_b + MAX_b) // 2
H = (MIN_H + MAX_H) // 2
h = (MIN_h + MAX_h) // 2

# Iterate through ranges, changing one variable at a time
for i in range(MAX_ITERATIONS):
    # Check if current values satisfy equation
    result = eqn(B, b, H, h)
    if result > TARGET and result < 10000000:
        print(f"Found solution after {i+1} iterations:")
        print(f"B = {B}, b = {b}, H = {H}, h = {h}")
        break

    # Change variables
    if result < TARGET:
        if B < MAX_B:
            B += 1
        elif b < MAX_b:
            b += 1
        elif H < MAX_H:
            H += 1
        elif h < MAX_h:
            h += 1
    else:
        if B > MIN_B:
            B -= 1
        elif b > MIN_b:
            b -= 1
        elif H > MIN_H:
            H -= 1
        elif h > MIN_h:
            h -= 1
