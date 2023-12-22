class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        ans = []
        for i in image:
            temp = reversed(i)
            ans.append([0 if num == 1 else 1 for num in temp])
        return ans