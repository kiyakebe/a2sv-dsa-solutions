class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        ans = []
        sum_of_even = 0
        for i in nums:
            if i % 2 == 0:
                sum_of_even += i

        for i in queries:
            if nums[i[1]] % 2 == 0:
                sum_of_even -= nums[i[1]]
            nums[i[1]] += i[0]

            if nums[i[1]] % 2 == 0:
                sum_of_even += nums[i[1]]
            ans.append(sum_of_even)
        return ans
