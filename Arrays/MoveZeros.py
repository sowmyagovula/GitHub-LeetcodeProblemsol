def MoveZeros(nums):
    l , r = 0,0
    while r < len(nums):
        if nums[r] != 0:
            temp = nums[r]
            nums[r] = nums[l]
            nums[l] = temp
            l +=1
            r +=1
        else:
            r += 1
    return nums


nums = [4,0,1,0,3,12]
Output = [4,1,3,12,0,0]

print(MoveZeros(nums))