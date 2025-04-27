def lengthOfLastWord(s):
    s = s.strip()
    words = s.split()
    return len(words[-1]) if words else 0

s = "Hello World"
Output = 5

print(lengthOfLastWord(s))


# Time complexity: O(1) Space complexity: O(1)
# ✅ Runtime 0ms Beats 100% Analyze Complexity Memory 18.98MB Beats 17.35%