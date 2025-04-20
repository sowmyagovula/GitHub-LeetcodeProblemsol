def SumDigitsRecursion(n):
    if n == 0:
        return 0
    else:
        return n % 10 + SumDigitsRecursion(n // 10)

n = 123
Output = 6

print(SumDigitsRecursion(n))