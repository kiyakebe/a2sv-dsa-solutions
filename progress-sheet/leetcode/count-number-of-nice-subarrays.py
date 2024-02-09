class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        left = 0
        ans = 0
        count = 0
        current = 0
        for right in range(len(nums)):
            if nums[right]%2 == 1:
                    count += 1
                    current = 0

            while(count == k):                
                if nums[left]%2 == 1:
                    count -= 1
                current += 1
                left += 1

            ans += current
     
        return ans