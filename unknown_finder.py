target = 6127552.083333333
min_target = 6127552.083333333
max_target = 10000000

# define the ranges for each variable
W_range = range(50, 151)
w_range = range(45, 141)
H_range = range(80, 201)
h_range = range(75, 191)


# initialize the best solution found so far
best_solution = None
best_diff = float('inf')

# iterate over all possible combinations of values, starting from the middle values of each range
for W in range(100, 50, -10):
    for w in range(93, 45, -10):
        for H in range(140, 80, -15):
            for h in range(133, 75, -15):
                # evaluate the equation for the current values of B, b, H, and h
                result = (W*pow(H,3)/12) - (w*pow(h,3)/12)

                # check if the result is within the target range and closer to the target than the best solution found so far
                if min_target < result < max_target and abs(target - result) < best_diff:
                    best_solution = (W, w, H, h)
                    best_diff = abs(target - result)

                # if the result is within the target range, we can stop searching
                if min_target < result < max_target:
                    break

            if best_solution:
                break

        if best_solution:
            break

    if best_solution:
        break

# iiterate over all possible combinations of values, starting from the middle values of each range
if not best_solution:
    for B in range(100, 151, 10):
        for b in range(93, 141, 10):
            for H in range(140, 201, 15):
                for h in range(133, 191, 15):
                    # evaluate the equation for the current values of B, b, H, and h
                    result = (B*pow(H,3)/12) - (b*pow(h,3)/12)

                    # check if the result is within the target range and closer to the target than the best solution found so far
                    if min_target < result < max_target and abs(target - result) < best_diff:
                        best_solution = (W, w, H, h)
                        best_diff = abs(target - result)

                    # if the result is within the target range, we can stop searching
                    if min_target < result < max_target:
                        break

                if best_solution:
                    break

            if best_solution:
                break

        if best_solution:
            break

# print the best solution found
if best_solution:
    print(f"The best solution found is B={best_solution[0]}, b={best_solution[1]}, H={best_solution[2]}, h={best_solution[3]}")
    print(f"The result is {result}")
else:
    print("No solution found within the given range and number of iterations.")


W=best_solution[0]
w=best_solution[1]
H=best_solution[2]
h=best_solution[3]