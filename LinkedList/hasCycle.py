class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def hasCycle(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True
    return False



# Time complexity: O(1) Space complexity: O(n)
# ✅ Runtime 48ms Beats 59% Analyze Complexity Memory 18.84MB Beats 54.81%