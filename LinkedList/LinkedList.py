class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def traverse(self):
        if self.head is None:
            print("Empty List")
            return
        a = self.head
        while a is not None:
            print(a.data, end= "-> ")
            a= a.next

    def insertBeg(self, data):
        nf = Node(data)
        nf.next = self.head
        self.head = nf

    def insertEnd(self, data):
        ne = Node(data)
        a = self.head
        while a.next is not None:
            a = a.next
        a.next = ne

    def insertMid(self, data, pos):
        np =Node(data)
        a= self.head
        for i in range(pos - 1):
            a = a.next
        np.next = a.next
        a.next = np

    def reverse(self):
        prev = None
        curr = self.head
        while curr is not None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node


if __name__ == "__main__":
    ll = LinkedList()
    ll.insertBeg(1)
    ll.insertBeg(66)
    ll.insertBeg("apple")
    ll.insertEnd(10)
    ll.insertMid("Middle3", 3)
    ll.traverse()
    ll.reverse()