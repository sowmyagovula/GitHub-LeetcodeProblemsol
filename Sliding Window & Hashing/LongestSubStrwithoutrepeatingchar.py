def lengthOfLongestSubstring(s):
    max_ = 0
    max_len = 0
    seen = set()
    left = 0

    for right in s:
        while right in seen:
            seen.remove(s[left])
            left += 1

        seen.add(right)
        max_ = len(seen)
        max_len = max(max_, max_len)

    return max_len


s = "pwwkew"
Output = 3

print(lengthOfLongestSubstring(s))