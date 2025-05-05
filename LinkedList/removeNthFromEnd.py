class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(head, n):
    length = 0
    curr = head

    while curr:
        length += 1
        curr = curr.next
    
    if n == length:
        return head.next
    
    curr = head
    for _ in range(length - n - 1):
        curr = curr.next

    curr.next = curr.next.next

    return head


# Time complexity: O(1) Space complexity: O(n)
# ✅ Runtime 0ms Beats 100% Analyze Complexity Memory 18.84MB Beats 14.81%