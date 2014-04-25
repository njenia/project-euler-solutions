required_sum = 1000

for a in range(1, required_sum):
    for b in range(a, required_sum):
        potential_c = required_sum - a - b
        if potential_c ** 2 == a ** 2 + b ** 2:
            print(str(a * b * potential_c))
            exit()