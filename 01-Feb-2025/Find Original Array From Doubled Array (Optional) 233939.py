# Problem: Find Original Array From Doubled Array (Optional) - https://leetcode.com/problems/find-original-array-from-doubled-array/

class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        n = len(changed)
        if n%2 == 1:
            return []
        
        changed.sort()
        counter = Counter(changed)
        ans = []

        for i in range(n):
            if counter[changed[i]] == 0:
                continue

            new_val = changed[i]*2
            counter[new_val] -= 1
            counter[changed[i]] -= 1

            if counter[new_val] < 0:
                return []
            
            ans.append(changed[i])
        
        return ans