def sum_digits(n):
    total = 0
    for digits in str(n):
        total += int(digits)
    return total

n = 121
print(sum_digits(n))