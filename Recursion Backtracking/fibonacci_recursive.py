def FibonacciSeriesRecursion(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return FibonacciSeriesRecursion(n-1) + FibonacciSeriesRecursion(n-2)
    
num = 10
for i in range(num):
    print(FibonacciSeriesRecursion(i), end=" ")
