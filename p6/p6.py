required_length = 100

sum_of_squares = 0
for num in range(required_length + 1):
    sum_of_squares += num ** 2

square_of_sums = 0
for num in range(required_length + 1):
    square_of_sums += num
square_of_sums **= 2

print(square_of_sums - sum_of_squares)