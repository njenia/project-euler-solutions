limit = 4000000
last_num = 1
new_num = 2
sum_of_even_fibonacci_numbers = 0
while new_num <= limit:
    if new_num % 2 == 0:
        print(new_num)
        sum_of_even_fibonacci_numbers += new_num
    last_num, new_num = new_num, new_num + last_num
    print(new_num)

print(sum_of_even_fibonacci_numbers)