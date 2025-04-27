def FrequencyMostFrequentElement(nums, k):
    nums.sort()
    n= len(nums)
    l , r = 0, 0
    res, total = 0, 0

    while r < len(nums):
        total += nums[r]
        print("total",total)
        while nums[r]* (r-l+1) > total+k:
            total -= nums[l]
            print("total2",total)
            l += 1

        res = max(res, r-l+1) 
        print("res", res)
        print("r-l+1", r-l+1)
        r += 1
    return res


nums = [1,4,8,13]
k = 5
Output = 2

print(FrequencyMostFrequentElement(nums, k))

# Time complexity: O(nlogn) Space complexity: O(n)
# ✅ Runtime 285ms Beats 53% Analyze Complexity Memory 28.98MB Beats 15.45%