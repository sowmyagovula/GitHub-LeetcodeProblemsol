def LongestCommonPrefix(strs):
    res = ""
    for i in range(len(strs[0])):
        for s in strs:
            if i == len(s) or s[i] != strs[0][i]:
                return res
            
        res += s[i]
    return res


# Time complexity: O(n^2) Space complexity: O(n)
# ✅ Runtime 0ms Beats 100% Analyze Complexity Memory 17.72MB Beats 79.06%%


 
strs = ["flower","flow","flight"]
Output = "fl"

print(LongestCommonPrefix(strs))
print(LongestCommonPrefix(strs)==Output)