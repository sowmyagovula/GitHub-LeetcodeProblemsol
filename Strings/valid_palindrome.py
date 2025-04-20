def isPalindrome(s):
    s = s.replace(" ", "")
    s = s.lower()
    l = 0
    r = len(s)-1
    while l < r:
        if not(s[l].isalnum()):
            l+=1
            continue
        if not(s[r].isalnum()):
            r-=1
            continue
        if s[l] != s[r]:
            return False
        l+=1
        r-=1
    return True



# Big-O-Notation O(n) time complexity, O(1) space complexity
# ✅ Runtime 7ms Beats 80.95% Analyze Complexity Memory 18.08MB Beats 70.24%


s = "A man, a plan, a canal: Panama"
Output= True

print(isPalindrome(s))