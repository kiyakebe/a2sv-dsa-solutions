class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l, r, position = 0, len(letters)-1, 0

        while l <= r:
            m = l+(r-l)//2

            if letters[m] == target:
                position = m+1
                l = m+1
            elif letters[m] < target:
                l = m+1
            else:
                position = m
                r = m-1

        if position == len(letters):
            return letters[0]
        return letters[position]
