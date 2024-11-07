# Problem: Insert Greatest Common Divisors in Linked List - https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node1 = head
        node2 = head.next

        while node1 and node2:
            val = gcd(node1.val, node2.val)
            new_node = ListNode(val, node2)
            node1.next = new_node

            node1 = node2
            node2 = node2.next
        
        return head