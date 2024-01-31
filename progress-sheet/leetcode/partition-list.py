# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        odd = ListNode()
        even = ListNode()
        od_p = odd
        ev_p = even
        temp = head

        while temp:
            if temp.val < x:
                odd.next = temp
                temp = temp.next
                odd = odd.next
                odd.next = None
            else:
                even.next = temp
                temp = temp.next
                even = even.next
                even.next = None

        odd.next = ev_p.next
        
        return od_p.next