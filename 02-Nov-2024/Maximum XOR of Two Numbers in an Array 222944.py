# Problem: Maximum XOR of Two Numbers in an Array - https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/

class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(2)]

class Solution:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, num):
        curr = self.root
        for i in range(32, -1, -1):
            idx = num & (1 << i) != 0
            if not curr.children[idx]:
                curr.children[idx] = TrieNode()

            curr = curr.children[idx]
    
    def findCurrXor(self, num):
        curr = self.root
        result = 0

        for i in range(32, -1, -1):
            idx = num & 1 << i != 0

            if idx == 1 and curr.children[0]:
                curr = curr.children[0]
            elif idx == 0 and curr.children[1]:
                result |= 1<<i
                curr = curr.children[1]
            elif idx == 1 and not curr.children[0]:
                result |= 1<<i           
                curr = curr.children[1]
            else:
                curr = curr.children[0]
            
            if not curr:
                break

        return result^num
            
    def findMaximumXOR(self, nums: List[int]) -> int:
        for num in nums:
            self.insert(num)
        
        max_xor = 0

        for num in nums:
            res = self.findCurrXor(num)
            max_xor = max(max_xor, res)
        
        return max_xor