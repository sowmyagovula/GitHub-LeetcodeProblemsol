class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(head, n):
    dummy = ListNode(0, head) 
    fast = slow = dummy

    for _ in range(n + 1):
        fast = fast.next
 
    while fast:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next

    return dummy.next 


def list_to_linkedlist(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    curr = head
    for val in arr[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head

def linkedlist_to_list(head):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res


head = list_to_linkedlist([1, 2, 3, 4, 5])
n = 2
new_head = removeNthFromEnd(head, n)
print(linkedlist_to_list(new_head)) 