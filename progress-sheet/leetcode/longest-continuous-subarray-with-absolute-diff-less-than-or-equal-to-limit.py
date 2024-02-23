class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_s = deque()
        min_s = deque()
        max_s.append(nums[0])
        min_s.append(nums[0])

        n = len(nums)
        max_len = 1
        l = 0

        for i in range(1, n):

            while max_s and nums[i] > max_s[-1]:
                max_s.pop()

            while min_s and nums[i] < min_s[-1]:
                min_s.pop()
                
            max_s.append(nums[i])
            min_s.append(nums[i])

            while max_s[0] - min_s[0] > limit:
                if nums[l] == max_s[0]:
                    max_s.popleft()
                if nums[l] == min_s[0]:
                    min_s.popleft()
                l += 1
            max_len = max(max_len, i-l+1)

        return max_len