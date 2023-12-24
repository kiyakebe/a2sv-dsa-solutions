class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = []

        nums_set = set()
        for i in nums:
            if i in nums_set:
                ans.append(i)
            nums_set.add(i)

        total_num_set = {x for x in range(1, n+1)}
        missing = total_num_set - nums_set

        ans.append(*missing)
        
        return ans