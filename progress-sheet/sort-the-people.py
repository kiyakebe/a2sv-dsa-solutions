class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        d = {heights[i]: names[i] for i in range(len(names))}
        heights.sort(reverse = True)
        ans = []
        for i in heights:
            ans.append(d[i])
        return ans