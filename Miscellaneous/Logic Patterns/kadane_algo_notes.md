# ⚡ Kadane's Algorithm - Maximum Subarray Sum

### 🧠 Problem:
Given an integer array `nums`, find the **contiguous subarray** (containing at least one number) which has the **largest sum** and return its sum.

📌 LeetCode Problem: [#53. Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)

---

## ✅ Kadane’s Algorithm - Core Idea:

At each element, you decide:
- Should I **continue** the current subarray, or
- Should I **start fresh** from this element?

---

### 🔧 Formula:


---

### 👣 Step-by-Step:

1. Initialize:
   ```python
   current_sum = max_sum = nums[0]
   ```
2. Iterate over the array from index 1:
    ```
    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    ```

3. Return max_sum


### Example:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6

### Why It Works:
Negative sums are discarded if the next element alone is greater.

Tracks the best sum so far efficiently.

Runs in O(n) time — fastest possible.



## ✅ Final Python Code:
def maxSubArray(nums):
    current_sum = max_sum = nums[0]
    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum
