def ReverseWordsString(s):
    s= s.strip()
    s= s.split()
    new_s = []
    for i in range(len(s)-1, -1, -1):
        new_s.append(s[i])

    return ' '.join(new_s)


# Time complexity: O(n) Space complexity: O(1)
# ✅ Runtime 0ms Beats 100% Analyze Complexity Memory 17.16MB Beats 69.66%%



s = "a good   example"
Output = "example good a"

print(ReverseWordsString(s))
print(ReverseWordsString(s)==Output)