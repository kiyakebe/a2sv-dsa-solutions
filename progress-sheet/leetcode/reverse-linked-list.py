# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ans = None

        while head:
            newNode = ListNode()
            newNode.val = head.val
            newNode.next = ans
            ans = newNode
            head = head.next

        if ans:
            return ans
        return None