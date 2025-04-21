def MaxSubarraySum(nums):
    max_sum = float('-inf')
    curr_sum = 0
    n = len(nums)

    for i in nums:
        curr_sum += i
        max_sum = max(curr_sum, max_sum)
        if curr_sum < 0 :
            curr_sum = 0
        
    return max_sum

nums = [-2,1,-3,4,-1,2,1,-5,4]
Output =  6

print(MaxSubarraySum(nums))
print(MaxSubarraySum(nums)==Output)
