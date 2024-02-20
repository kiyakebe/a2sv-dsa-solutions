class Solution:
    def minimumSteps(self, s: str) -> int:
        b_count = 0
        count = 0
        for i in s:
            if i == '1':
                b_count += 1
            else:
                count += b_count
        return count