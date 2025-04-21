def RemoveDuplicateSortedArray(nums):
    left = 1
    for right in range(1, len(nums)):
        if nums[right] != nums[right - 1]:
            nums[left] = nums[right]
            left += 1
    return left


# Time complexity: O(n) Space complexity: O(1)
# ✅ Runtime 0ms Beats 100% Analyze Complexity Memory 18.98MB Beats 49.35%




nums = [1,1,2]
Output = 5
# nums = [1,2]
print(RemoveDuplicateSortedArray(nums))