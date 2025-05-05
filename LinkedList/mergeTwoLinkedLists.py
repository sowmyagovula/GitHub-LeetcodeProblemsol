class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def mergeTwoLinkedLists(self, l1, l2):
    dummy = Node(-1)
    tail = dummy

    while l1 and l2:
        if l1.data < l2.data:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    tail.next = l1 if l1 else l2

    return dummy.next



# Time complexity: O(1) Space complexity: O(n)
# ✅ Runtime 0ms Beats 100% Analyze Complexity Memory 18.84MB Beats 14.81%