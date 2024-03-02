# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # m = len-> headA
        m = 0
        # n = len-> headB
        n = 0

        tempA = headA
        while tempA:
            m += 1
            tempA = tempA.next
        tempB = headB
        while tempB:
            n += 1
            tempB = tempB.next
        
        if tempA != tempB:
            return -1

        if m > n:
            d = m - n
            while d:
                headA = headA.next
                d -= 1
        else:
            d = n - m
            while d:
                headB = headB.next
                d -= 1
        while headA and headB:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next