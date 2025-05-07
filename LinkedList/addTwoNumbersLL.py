class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    s1, s2 = [], []
    while l1:
        s1.append(l1.val)
        l1 = l1.next
    while l2:
        s2.append(l2.val)
        l2 = l2.next

    carry = 0
    result = None

    while s1 or s2 or carry:
        x = s1.pop() if s1 else 0
        y = s2.pop() if s2 else 0

        total = x + y + carry
        carry = total // 10
        node = ListNode(total % 10)

        node.next = result
        result = node

    return result

l1 = [7,2,4,3]
l2 = [5,6,4]
Output= [7,8,0,7]

print(addTwoNumbers(l1, l2))

# Time complexity: O(2n) Space complexity: O(n)
# ✅ Runtime 3ms Beats 90% Analyze Complexity Memory 20.84MB Beats 40.81%