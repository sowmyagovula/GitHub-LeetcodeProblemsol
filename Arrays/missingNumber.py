'''
def missingNumber(nums):
    numbers = sorted(nums)
    if numbers == nums and len(numbers) > 1:
        if numbers[0] == 0:
            return numbers[-1]+1
        else:
            return 0
    if len(numbers)== 1:
        if numbers[0] == 0:
            return numbers[-1]+1
        else:
            return 0
    for i in range(1, len(numbers)):
        if numbers[i]-1 != numbers[i-1]:
            return numbers[i]-1
    return 0
'''


def missingNumber(nums):
    res = len(nums) # 2
    for i in range(len(nums)):
        res += (i - nums[i])
        print(res)
    return res

nums = [9,6,4,2,3,5,7,0,1]
Output = 2

print(missingNumber(nums))

# Time complexity: O(n) Space complexity: O(1)
# ✅ Runtime 28ms Beats 16.80% Analyze Complexity Memory 19.04MB Beats 11.22%