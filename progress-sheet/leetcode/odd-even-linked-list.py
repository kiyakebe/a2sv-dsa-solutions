# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd = ListNode()
        even = ListNode()
        ev_p = even
        temp = head
        while temp:
            odd.next = temp
            temp = temp.next
            odd = odd.next
            odd.next = None
            if temp:
                even.next = temp
                temp = temp.next
                even = even.next
                even.next = None

        odd.next = ev_p.next
        return head