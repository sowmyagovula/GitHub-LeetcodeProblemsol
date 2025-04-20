def twoSum(nums, target):
    sorted_nums= sorted(nums)
    print(nums)
    right = len(nums) - 1
    left = 0
    while left < right:
        sum = sorted_nums[left] + sorted_nums[right]
        if sum == target:
            if sorted_nums != nums:
                x = nums.index(sorted_nums[left]) # [3-- 2 3]
                y = nums.index(sorted_nums[right]) # [3-- 2 3]
                if x == y:
                    y = nums.index(sorted_nums[right], x + 1) # [3-- 2 3]
                return [x, y]
            return [left, right]
        elif sum < target:
            left += 1
        else:
            right -= 1
    return []

# O(n) time complexity, O(n) space complexity
# ✅ Runtime 0ms Beats 100.00% Analyze Complexity Memory 18.50MB Beats 72.74%


nums = [3,2,3]
target = 6
Output = [0,2]
print(twoSum(nums, target))
print(twoSum(nums, target)==Output)





# ❎ Only to copy and paste