def MoveZeroes(nums):
    left = 0
    right = 0

    while right < len(nums):
        if nums[right] != 0:
            temp = nums[left]
            nums[left] = nums[right]
            nums[right] = temp

            left += 1
            right += 1
        elif nums[right] ==0:
            right += 1
    
    return nums


# Time complexity: O(n) Space complexity: O(n)
# ✅ Runtime 11ms Beats 24% Analyze Complexity Memory 18.16MB Beats 31.67%


nums = [0,1,0,3,12]
Output= [1,3,12,0,0]

print(MoveZeroes(nums))
print(MoveZeroes(nums)==Output)