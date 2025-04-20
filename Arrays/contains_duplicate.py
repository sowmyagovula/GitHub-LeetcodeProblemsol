def ContainsDuplicate(nums):
    nums_set = set(nums)
    return len(nums) != len(nums_set)
    # 1234
    

# Time complexity: O(1) Space complexity: O(n)
# ✅ Runtime 8ms Beats 72.48% Analyze Complexity Memory 31.64MB Beats 29.54%

def ContainsDuplicate2(nums):
    res = []
    for i in nums:
        if i not in res:
            res.append(i)
        else:
            return True
    return False


# ✅ Time complexity: O(n) Space complexity: O(n)




nums = [1,2,3,4]
Output = False

print(ContainsDuplicate(nums))
print(ContainsDuplicate(nums)==Output)

print(ContainsDuplicate2(nums))
print(ContainsDuplicate2(nums)==Output)