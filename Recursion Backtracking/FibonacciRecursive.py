
"""
def fibonacci(num):
    if num == 0:
        return 0
    if num == 1:
        return 1
    return fibonacci(num-1)+fibonacci(num-2)

for i in range(10):
    print(fibonacci(i), end=" ")
"""

class Solution:
    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        return self.fib(n-1) + self.fib(n-2)
    
# Time complexity: O(2^n) Space complexity: O(n)
# ✅ Runtime 368ms Beats 13.21% Analyze Complexity Memory 17.58MB Beats 89.36%

