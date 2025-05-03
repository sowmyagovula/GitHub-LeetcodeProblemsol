def FizzBuzz(num):
    for n in range(1, num+1):
        if n % 3 == 0 and n % 5 == 0:
            print("FizzBuzz", end= " ")
        elif n % 3 == 0:
            print("Fizz", end= " ")
        elif n % 5 == 0:
            print("Buzz", end= " ")
        else:
            print(n, end= " ")

print(FizzBuzz(100))