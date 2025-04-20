def PalindromeStringRecursion(s):
    if len(s)<=1:
        return True
    if s[0] != s[-1]:
        return False
    
    return PalindromeStringRecursion(s[1:-1])

s = "ana"
Output = True
print(PalindromeStringRecursion(s))