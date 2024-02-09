def solve(numheads, numlegs):
    chicken = 0
    rabbit = 0
    for chicken in range(numheads + 1):
        rabbit = numheads - chicken
        total_legs = (chicken * 2) + (rabbit * 4)
        if total_legs == numlegs:
            return chicken, rabbit
    return None, None

chickens, rabbits = solve(35, 94)
if chickens is not None and rabbits is not None:
    print(f"Number of chickens: {chickens}")
    print(f"Number of rabbits: {rabbits}")
else:
    print("No solution")