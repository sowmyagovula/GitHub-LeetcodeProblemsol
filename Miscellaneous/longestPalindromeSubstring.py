"""

def longestPalindromeSubstring(s):
    def palindrome(left, right):
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
    l= 0
    r= len(s)-1
    while l<=r:
        if s[l] == s[r]:
            if palindrome(l, r):
                return s[l:r+1]
            else:
                l += 1
                r -= 1
        else:
            l += 1
            r -= 1  
    return 0

"""



"""
def longestPalindromeSubstring(s):
    def expanding(s, l, r):
        ss = ""
        max_len = 0
        while l>=0 and r<len(s) and s[l]== s[r]:
            if r - l + 1 > max_len:
                max_len = r - l + 1
                ss= s[l:r+1]
            l -=1
            r +=1
        return ss
    
    result = ""
    for i in range(len(s)):
        odd = expanding(s, i, i)
        even = expanding(s, i, i+1)
        if len(odd) > len(result):
            result = odd        
        if len(even) > len(result):
            result = even
    return result
"""



def longestPalindromeSubstring(s):
    n = len(s)
    max_len = ""
    def palindrome(i,j):
        while (i>=0 and j<n and s[i]==s[j]):
            i-=1
            j+=1       
        return s[i+1:j]
    
    for i in range(n):
        x = palindrome(i,i)
        y = palindrome(i, i+1)

        if len(x)>len(y) and len(x)>len(max_len):
            max_len = x
        elif len(y)>len(x) and len(y)>len(max_len):
            max_len= y
    return max_len


# Time complexity: O(n) Space complexity: O(n)
# ✅ Runtime 539ms Beats 38.80% Analyze Complexity Memory 18.04MB Beats 29.22%

    
s = "ac"
Output = "bab"
print(longestPalindromeSubstring(s))  # Expected Output: "bab" or "aba"