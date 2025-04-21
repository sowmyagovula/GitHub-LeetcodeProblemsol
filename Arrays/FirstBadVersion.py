def isBadVersion(num):
     if num == 4:
          return True
     elif num > 4:
          return True
     else:
          return False


def firstBadVersion(n: int) -> int:
    left = 1
    right = n
    while left < right:
        mid = (right+left)//2
        if isBadVersion(mid):
            right = mid
        else:
            left = mid + 1
    return left

print(firstBadVersion(5))

# 1 2 3 4 5


# Time complexity: O(n) Space complexity: O(1)
# ✅ Runtime 38ms Beats 51.06% Analyze Complexity Memory 17.64MB Beats 68.87%
