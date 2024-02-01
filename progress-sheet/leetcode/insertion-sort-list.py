# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def prevs(prev, node):
            node.prev = prev
        head.prev = None
        prev = head

        while prev.next:
            prevs(prev, prev.next)
            prev = prev.next
        left = head
        while left:
            right = left.next
            while right and right.prev and right.val < right.prev.val:
                right.val, right.prev.val = right.prev.val, right.val
                right = right.prev
            left = left.next
        while left and left.prev:
            left = left.prev
        return head
            
        
        # while prev:
        #     print(prev.val, "->", end="")
        #     prev = prev.prev
        
        return