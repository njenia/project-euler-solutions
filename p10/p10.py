import math
number = 2000000

def calculate_sum_of_primes_under(number):
    numbers = [True] * number
    upper_limit = math.ceil(math.sqrt(number))
    for i in range(2, upper_limit):
        if not numbers[i - 2]:
            continue
        for j in range(2 * i - 2, number, i):
            numbers[j] = False
    sum = 0
    for index, is_prime in enumerate(numbers):
        if is_prime:
            sum += index + 2
    return sum

print(str(calculate_sum_of_primes_under(number)))