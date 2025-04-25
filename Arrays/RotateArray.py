"""


# By using return

def RotateArray(nums, k):
    return nums[-k:]+nums[:-k]



from collections import deque
def RotateArray(nums, k):
    nums = deque(nums)
    n = len(nums)
    for i in range(k):
        nums.appendleft(nums[-1])
        if nums[i] in nums:
            nums.pop()
    print(nums)

# Its correct but Its not changing in-place

"""

def RotateArray(nums, k):

    k %= len(nums)

    def reverse(left, right):
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
    
    reverse(0, len(nums)-1)
    reverse(0, k-1)
    reverse(k, len(nums)-1)


    print(nums)


# Time complexity: O(1) Space complexity: O(1)
# ✅ Runtime 10ms Beats 24.86% Analyze Complexity Memory 25.77MB Beats 21.99%


nums = [1,2,3,4,5,6,7]
k = 3
Output = [5,6,7,1,2,3,4]


print(RotateArray(nums, k))