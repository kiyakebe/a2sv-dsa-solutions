class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.dummy = Node()
        self.size = 0

    def get(self, index: int) -> int:
        if index < self.size:
            curr = self.dummy.next
            for i in range(index):
                curr = curr.next
            return curr.val
        return -1

    def addAtHead(self, val: int) -> None:
        self.dummy.next = Node(val, self.dummy.next)
        self.size += 1
        # self.display(self.dummy.next)

    def addAtTail(self, val: int) -> None:
        curr = self.dummy
        while curr.next:
            curr = curr.next
        curr.next = Node(val)
        self.size += 1
        # self.display(self.dummy.next)

    def addAtIndex(self, index: int, val: int) -> None:
        curr = self.dummy
        if index < self.size:
            while index != 0:
                curr = curr.next 
                index -= 1
            curr.next = Node(val, curr.next)
            self.size += 1
            # self.display(self.dummy.next)
        else:
            if index == self.size:
                self.addAtTail(val)

    def deleteAtIndex(self, index: int) -> None:
        curr = self.dummy.next
        prev = self.dummy
        if index < self.size:
            while index != 0:
                prev = curr
                curr = curr.next
                index -= 1
            if curr:
                prev.next = curr.next
            self.size -= 1

        # self.display(self.dummy.next)

    # def display(self, head):
    #     while head:
    #         print(head.val, "->", end="")
    #         head = head.next
    #     print("")

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)