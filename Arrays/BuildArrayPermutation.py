def BuildArrayPermutation(nums):
    ans = [0]*len(nums)

    for i in range(len(nums)):
        ans[i] = nums[nums[i]]

    return ans

nums = [0,2,1,5,3,4]
Output = [0,1,2,4,5,3]

print(BuildArrayPermutation(nums))

# Time complexity: O(n) Space complexity: O(1)
# ✅ Runtime 3ms Beats 46% Analyze Complexity Memory 17.98MB Beats 97.35%