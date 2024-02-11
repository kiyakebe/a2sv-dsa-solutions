class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        
        for i in range(1,len(nums)):
            nums[i] += nums[i-1]

        freq = defaultdict(int)
        freq[0] = 1
        count = 0

        for i, num in enumerate(nums):
            count += freq[num%k]
            freq[num%k] += 1
        
        return count