class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        k_sum = 0
        for i in range(k):
            k_sum += nums[i]
        
        max_sum = k_sum
        for i in range(k, len(nums)):
            k_sum -= nums[i-k]
            k_sum += nums[i]
            max_sum = max(max_sum, k_sum)
        
        return max_sum / k
