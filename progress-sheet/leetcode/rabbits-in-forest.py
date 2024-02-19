class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = Counter(answers)
        number = 0

        for v,c in count.items():
            if v == 0:
                number += c
            elif c <= v+1:
                number += v+1
            else:
                val = ceil(c/(v+1))*(v+1) 
                number += val
        return number