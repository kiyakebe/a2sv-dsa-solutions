# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = head
        slow = head
        l = 0

        if not head.next:
            return None

        while fast and n > 0:
            fast = fast.next
            n -= 1

        while fast and fast.next:
            fast = fast.next
            slow = slow.next

        if slow == head:
            if fast == head:
                head = head.next
            elif fast == None:
                head = head.next
            else:
                head.next = head.next.next
        else:
            if slow == head:
                head = head.next
            elif slow and slow.next:
                slow.next = slow.next.next
        
        return head