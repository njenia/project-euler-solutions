limit = 1000
factor_1 = 3
factor_2 = 5

def calculate_sum_of_divisors(factor_1, factor_2, limit):
    divisors = [num for num in range(limit) if (num % factor_1 == 0 or num % factor_2 == 0)]
    sum = 0
    for divisor in divisors:
        sum += divisor
    return sum

print(str(calculate_sum_of_divisors(factor_1, factor_2, limit)))