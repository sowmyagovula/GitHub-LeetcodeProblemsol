def SubarraySumEqualsK(nums, k):
    count = 0

    total = 0
    for i in range(0, len(nums)):
        for j in range(i, len(nums)):
            count += nums[j]
            print('count', count)
        if count == k:
            total += 1
        count = 0
    return total

nums = [1,1,1]
k = 2
Output = 2

print(SubarraySumEqualsK(nums, k))