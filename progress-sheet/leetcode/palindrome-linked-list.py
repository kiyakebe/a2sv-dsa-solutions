# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        n = 0
        # count the length
        cur = head
        while cur:
            cur = cur.next
            n+=1
        
        fast = head
        slow = head
        st = []

        while fast and fast.next:
            st.append(slow.val)
            fast = fast.next.next
            slow = slow.next
        # pass the middle element of it is odd
        if n%2 != 0:
            slow = slow.next
        # check for pallindrome
        while slow:
            if slow.val == st[-1]:
                st.pop()
                slow = slow.next
            else:
                return False

        return True
'''
O(n) time and O(1) space ca be 
acheived using fast and slow method

handle one element
1
and odd and even length separatly
1 2 1
'''