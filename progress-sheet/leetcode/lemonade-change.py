class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        
        changes = {
            5: 0,
            10: 0,
            20: 0
        }

        for i in bills:
            changes[i] += 1
            v = i-5
            if v == 5:
                if changes[5] < 1:
                    return False
                changes[5] -= 1
            elif v == 15:
                if changes[10] < 1:
                    if changes[5] < 3:
                        return False
                    changes[5] -= 3
                else:
                    if changes[5] < 1:
                        return False
                    changes[10] -= 1
                    changes[5] -= 1
        return True
                


