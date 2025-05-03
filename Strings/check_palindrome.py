def check_palindrome(s):
    s = str(s)
    s_ = s[::-1]
    return s == s_

input = "malayalam"
input2 = 12321

print(check_palindrome(input))
print(check_palindrome(input2))