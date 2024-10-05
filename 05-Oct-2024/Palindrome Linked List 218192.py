# Problem: Palindrome Linked List - https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        st = []
        fast = head
        slow = head
        n = 0
        while fast:
            st.append(slow.val)
            slow = slow.next
            fast = fast.next
            if fast:
                fast = fast.next
                n += 1
            n += 1
        
        if n%2 == 1:
            st.pop()
        
        while slow:
            if st[-1] == slow.val:
                st.pop()
                slow = slow.next
            else:
                return False
        
        return True