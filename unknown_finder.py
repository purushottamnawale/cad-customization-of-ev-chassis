min_lhs = 6127552.083333333
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


print(W, H, w, h)
