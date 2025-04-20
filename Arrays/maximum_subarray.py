def MaximumSubarray(nums):
    max_sum = float('-inf')
    current_sum = 0
    for right in nums:
        current_sum += right
        
        max_sum = max(max_sum, current_sum)
        if current_sum < 0:
            current_sum = 0
    return max_sum



# Big-O-Notation O(n) time complexity, O(1) space complexity
# ✅ Runtime 53ms Beats 69.98% Analyze Complexity Memory 23.80MB Beats 23.56%


nums = [-1]
Output = 6

print(MaximumSubarray(nums))
print(MaximumSubarray(nums)==Output)