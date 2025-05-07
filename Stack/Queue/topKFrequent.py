from collections import Counter
import heapq

def top_k_frequent(nums, k):
    counts = Counter(nums)
    return heapq.nlargest(k, counts, key=counts.get)


nums = [5,1,1,1,2,2,3]
k = 2
Output = [1,2]

print(top_k_frequent(nums, k))


# Time complexity: O(1) Space complexity: O(n)
# ✅ Runtime 3ms Beats 90% Analyze Complexity Memory 20.84MB Beats 40.81%