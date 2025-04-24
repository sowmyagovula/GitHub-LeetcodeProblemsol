"""

# Brute-force Method ⭐⭐⭐⭐⭐

def SlidingWindowMaximum(nums, k):
    total_max = []
    max_ = float('-inf')
    for i in range(0,len(nums)-k+1):
        for j in range(i,i+k):
            if nums[j] > max_:
                max_ = nums[j]
        total_max.append(max_)
        max_ = float('-inf')
    return total_max


def SlidingWindowMaximum(nums, k):
    all_max = []
    max_num = float('-inf')
    left = 0
    right = 0
    
    while right < len(nums)+1:
        if right - left >= k:
            all_max.append(max_num)
            max_num = float('-inf')
            left += 1
            right -= k-1
            # print(left , right )
            if left == len(nums)-k+1: 
                return all_max
        else:
            max_num = max(nums[right], max_num)
            # print("max ", max_num)
            right += 1
            # print('down', left , right )
        
    return all_max
 
 ### Working better sol
 ## Optimal using monotonic queue/ deque

"""




from collections import deque
def SlidingWindowMaximum(nums):
    q = deque()
    total = []
    l = r = 0

    while r < len(nums):
        while q and nums[q[-1]] < nums[r]:
            print("queue inside while", q)
            q.pop()
            print("queue inside while after pop", q)
        q.append(r)
        print("queue", q)

        if l > q[0]:
            q.popleft()

        if (r+1) >= k:
            total.append(nums[q[0]])
            print('total append', r, l, nums[q[0]])
            l += 1
        r+=1

    return total


nums = [1,3,-1,-3,5,3,6,7]
k = 3
Output = [3,3,5,5,6,7]

print(SlidingWindowMaximum(nums))