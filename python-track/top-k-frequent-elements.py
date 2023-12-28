class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_count  = Counter(nums)
        most_freq_k = [key for key, _ in nums_count.most_common(k)]

        return most_freq_k