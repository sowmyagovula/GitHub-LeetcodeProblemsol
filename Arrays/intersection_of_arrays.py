"""
def IntersectionTwoArrays(nums1, nums2):
    intersect = set()
    for i in nums1:
        for j in nums2:
            if i == j:
                intersect.add(i)
                break
    list_intersect = list(intersect)
    return list_intersect
"""

# Time complexity: O(n^2) Space complexity: O(n^2)
# ❎ Runtime 19ms Beats 5.59% Analyze Complexity Memory 17.50MB Beats 71.86%



def IntersectionTwoArrays(nums1, nums2):
    nums1_set = set(nums1)
    nums2_set = set(nums2)    
    res=[]
    for i in nums2_set:
        if i in nums1_set:
            res.append(i)
    return res


# Time complexity: O(n) Space complexity: O(n)
# ✅ Runtime 0ms Beats 100% Analyze Complexity Memory 18.16MB Beats 25.67%


nums1 = [1,2,2,1]
nums2 = [2,2]
Output = [2]

print(IntersectionTwoArrays(nums1, nums2))