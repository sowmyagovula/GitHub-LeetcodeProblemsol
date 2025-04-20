def MaximumNumVowelsSubstringFixedLength(s, k):
    curr , max_c = 0, 0
    vowels = {'a', 'e' ,'i', 'o', 'u'}
    for i in range(len(s)):
        if s[i] in vowels:
            curr += 1
        if i >= k and s[i-k] in vowels:
            curr -= 1
        i += 1
        max_c = max(max_c, curr)

        if max_c == k:
            return max_c

    return max_c



# Big-O-Notation O(n) time complexity, O(n) space complexity
# ✅ Runtime 108ms Beats 26.26% Analyze Complexity Memory 17.78MB Beats 88.65% 


s = "abciiidef"
k = 3
Output = 3

print(MaximumNumVowelsSubstringFixedLength(s, k))
# print(MaximumNumVowelsSubstringFixedLength(s, k)==Output)