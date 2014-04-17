import math

num = 600851475143

def is_prime_number(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

for possible_factor in reversed(range(math.ceil(math.sqrt(num)))):
    if num % possible_factor == 0 and is_prime_number(possible_factor):
        print(possible_factor)
        break