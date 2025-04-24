def productExceptSelf(nums):
    output = [1]* (len(nums))
    prefix = [1]* (len(nums)+1)
    for i in range(len(nums)):
        prefix[i+1] = prefix[i] * nums[i]
    suffix = 1
    for j in range(len(nums)-1 , -1, -1):
        output[j]= prefix[j] * suffix
        suffix = suffix * nums[j]
    return output


# Time complexity: O(2n) Space complexity: O(n)
# ✅ Runtime 26ms Beats 50.86% Analyze Complexity Memory 25.21MB Beats 35.23%




nums = [1,2,3,4]
Output = [24,12,8,6]


print(productExceptSelf(nums))
print(productExceptSelf(nums)==Output)