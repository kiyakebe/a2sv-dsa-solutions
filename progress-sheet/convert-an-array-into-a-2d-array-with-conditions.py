class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        d = Counter(nums)
        l = max(d.values())
        ans = []
        for i in range(l):
            temp = []
            for j in d:
                if d[j] != 0:
                    temp.append(j)
                    d[j] -= 1

            ans.append(temp)
        return ans