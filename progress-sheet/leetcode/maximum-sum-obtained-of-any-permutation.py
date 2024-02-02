class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        qp = [0 for i in range(n)]
        
        for l, r in requests:
            qp[l] += 1
            if r < n-1:
                qp[r+1] -= 1

        for i in range(1, n):
            qp[i] += qp[i-1]

        nums.sort(reverse=True)
        qp.sort(reverse=True)

        max_sum = 0

        for i in range(n):
            if qp[i]>0:
                max_sum += nums[i]*qp[i]
            else:
                break
        return max_sum % (10**9+7)