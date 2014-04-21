requested_prime_order = 10001

primes_list = [2]


def is_prime(smaller_primes, number):
    for prime in smaller_primes:
        if number % prime == 0:
            return False
    return True

non_prime_temp_count = 1
while len(primes_list) < requested_prime_order:
    next_potential_prime = primes_list[-1] + non_prime_temp_count
    if is_prime(primes_list, next_potential_prime):
        primes_list.append(next_potential_prime)
        non_prime_temp_count = 1
    else:
        non_prime_temp_count += 1

print(str(primes_list[-1]))