"""
def MaxAvgSubarray(nums, k):
    sum_4 = 0
    avg_4 = 0
    max_avg = 0
    left = 0

    if len(nums)==1 and k == 1:
        return nums[0]

    for right in range(left, len(nums)):
        if right - left >= k:
            avg_4 = sum_4/k
            max_avg = max(avg_4, max_avg)
            sum_4 = sum_4 - nums[left]
            left += 1
                
        sum_4 += nums[right]
        # print(left, right, right-left, right-left==k, nums[right], sum_4)
        
    return max_avg

"""

def MaxAvgSubarray(nums, k):
    win_sum = sum(nums[:k])
    max_sum = win_sum

    for i in range(k, len(nums)):
        win_sum += nums[i]
        win_sum -= nums[i-k]
        max_sum = max(win_sum, max_sum)
    return max_sum/k



# Time complexity: O(n) Space complexity: O(1)
# ✅ Runtime 90ms Beats 44.28% Analyze Complexity Memory 27.35MB Beats 78.45%



nums = [5]
k = 1
Output = 12.75000

print(MaxAvgSubarray(nums, k))
print(MaxAvgSubarray(nums, k)==Output)