def IsSubsequence(s, t):
    i, j = 0, 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1
    return True if i == len(s) else False



# Time complexity: O(n) Space complexity: O(n)
# ✅ Runtime 0ms Beats 100% Analyze Complexity Memory 17.16MB Beats 69.66%%



s = "abc"
t = "ahbgdc"
Output = True

print(IsSubsequence(s, t))
print(IsSubsequence(s, t)==Output)