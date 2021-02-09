def sum_of_digits_iteration(num):
    sum = 0
    while num != 0:
        last_digit = num % 10
        num = num // 10
        sum+=last_digit
    return sum

def sum_of_digits_recursion(num):
    assert num > 0 and int(num) == num, "Only positive integers"
    if num == 0:
        return 0
    return sum_of_digits_recursion(num//10) + num % 10

print(sum_of_digits_recursion(176))