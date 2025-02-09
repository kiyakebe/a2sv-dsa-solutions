# Problem: Spiral Matrix IV - https://leetcode.com/problems/spiral-matrix-iv/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        m1, m2 = 0, m-1
        n1 ,n2 = 0, n-1
        x = 0

        ans = [[-1 for _ in range(n)] for _ in range(m)]

        while m2>=m1 and n2>=n1 and head:
            if x%4 == 0:
                for i in range(n1, n2+1):
                    if not  head:
                        break
                    ans[m1][i] = head.val
                    head = head.next
                    
                m1 += 1
            elif x%4 == 1:
                for i in range(m1, m2+1):
                    if not  head:
                        break
                    ans[i][n2] = head.val
                    head = head.next
                n2 -= 1
            elif x%4 == 2:
                for i in range(n2, n1-1, -1):
                    if not  head:
                        break
                    ans[m2][i] = head.val
                    head = head.next
                m2 -= 1
            else:
                for i in range(m2, m1-1, -1):
                    if not  head:
                        break
                    ans[i][n1] = head.val
                    head = head.next
                n1 += 1
            x += 1
        return ans