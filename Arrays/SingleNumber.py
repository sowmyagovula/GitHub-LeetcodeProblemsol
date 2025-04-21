def SingleNumber(nums):
    xor = 0
    for i in nums:
        xor ^= i
    return xor


# ✅ Runtime 3ms Beats 65% Analyze Complexity Memory 19.98MB Beats 22.35%

nums = [2,2,1]
Output = 1

print(SingleNumber(nums))