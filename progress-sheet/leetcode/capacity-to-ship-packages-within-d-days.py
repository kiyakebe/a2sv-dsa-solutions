class Solution:
    def __init__(self):
        self.min_capacity = -1
    
    def check(self, weights, mid, left, right):
        calculated_days = 1
        counter = 0

        for i in range(len(weights)):
            counter += weights[i]
            if counter > mid:
                calculated_days += 1
                counter = weights[i]

        return calculated_days
        

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = max(weights), sum(weights)

        while left <= right:
            mid = left + (right-left) // 2

            if self.check(weights, mid, left, right) > days:
                left = mid+1
            else:
                right = mid-1
                best = mid

        return best