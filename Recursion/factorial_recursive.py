def FactorialRecursion(n):
    if (n == 1 or n == 0):
        return 1
    else:
        return (n * FactorialRecursion(n-1))
    
# Time complexity: O(n) Space complexity: O(n)
# ✅ 
    

n = 5
Output = 120
print(FactorialRecursion(n))
print(FactorialRecursion(n)== Output)

