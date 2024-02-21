class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        answer = 0
        curr = nums[-1]
        
        for i in range(len(nums)-1, -1, -1):
            if nums[i] <= curr:
                curr = nums[i]
                continue

            number_of_element = ceil(nums[i]/curr)
            curr = nums[i] // number_of_element

            answer += number_of_element-1

        return answer
