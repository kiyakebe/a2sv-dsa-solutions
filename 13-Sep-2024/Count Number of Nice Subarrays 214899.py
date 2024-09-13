# Problem: Count Number of Nice Subarrays - https://leetcode.com/problems/count-number-of-nice-subarrays/

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        left = 0
        right = 0
        cnt = 0
        ans = 0

        while left < len(nums) and right < len(nums):
            if nums[right]%2 == 1:
                cnt += 1
            
            right += 1

            if cnt == k:
                cnt_left = 1
                cnt_right = 1

                while left < right:
                    if nums[left]%2 == 0:
                        cnt_left += 1
                        left += 1
                    else:
                        cnt -= 1
                        left += 1
                        break

                while right < len(nums):
                    if nums[right]%2 == 0:
                        cnt_right += 1
                        right += 1
                    else:
                        break

                ans += (cnt_left*cnt_right)
        
        return ans