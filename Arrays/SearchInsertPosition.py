def SearchInsertPosition(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (right+left)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    if nums[mid] < target:
        return mid + 1
    else:
        return mid



# Time complexity: O(log N) Space complexity: O(1)
# ✅ Runtime 0ms Beats 100% Analyze Complexity Memory 18.98MB Beats 94.35%



nums = [1,3,5,6]
target = 2
Output = 4

print(SearchInsertPosition(nums, target))
print(SearchInsertPosition(nums, target)==Output)