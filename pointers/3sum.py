def Sum3(nums):
    nums.sort()
    res = []
    n = len(nums)
    for i, a in enumerate(nums):
        if i>0 and a == nums[i-1]:
            continue
        left = i+1
        right = n-1
        while left < right:
            summ = a + nums[left] + nums[right]
            if summ > 0:
                right -=1
            elif summ < 0:
                left += 1
            else:
                res.append([nums[i], nums[left], nums[right]])
                left+=1
                while nums[left] == nums[left-1] and left<right:
                    left+=1
    return res


nums = [2,-3,0,-2,-5,-5,-4,1,2,-2,2,0,2,-4,5,5,-10]
Output = [[-1,-1,2],[-1,0,1]]

print(Sum3(nums))


# Time complexity: O(n^2) Space complexity: O(n)
# ✅ Runtime 527ms Beats 76% Analyze Complexity Memory 20.84MB Beats 69.81%