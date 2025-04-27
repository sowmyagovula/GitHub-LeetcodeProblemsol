def recursiveBinarySearch(nums, t, st, ed):
    if len(nums) == 0:
        return False
    mid = (st+ed) // 2
    if nums[mid] == t:
        return mid
    elif nums[mid] < t:
        return recursiveBinarySearch(nums, t, mid+1, ed)
    else:
        return recursiveBinarySearch(nums, t, st, mid-1)

nums = [1,3,4,6,9,11,14,15,20]
t = 20

print(recursiveBinarySearch(nums, t, 0, len(nums)-1))