required_length = 3
largest = 10 ** required_length


def is_palindrome(multiplication_result):
    return str(multiplication_result)[::-1] == str(multiplication_result)

palindromes_list = []

for factor1 in reversed(range(largest)):
    for factor2 in reversed(range(largest)):
        multiplication_result = factor1 * factor2
        if len(str(factor1)) == required_length and len(str(factor2)) == required_length  \
                and is_palindrome(multiplication_result):
            palindromes_list.append(multiplication_result)

print(str(max(palindromes_list)))

