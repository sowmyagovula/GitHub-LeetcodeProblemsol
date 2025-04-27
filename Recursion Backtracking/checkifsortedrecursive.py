def checkifsortedrecursive(nums):
    if len(nums)==1 or len(nums)==0:
        return True
    return nums[0] < nums[1] and checkifsortedrecursive(nums[1:])

nums = [1,8,2,3,4,5]
print(checkifsortedrecursive(nums))