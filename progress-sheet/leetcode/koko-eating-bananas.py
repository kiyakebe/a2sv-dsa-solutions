class Solution:
    def check(self, piles, mid):
        hour_count = 0
        for i in piles:
            hour_count += ceil(i/mid)
        
        return hour_count

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right, best = 1, max(piles), -1

        while left <= right:
            mid = left + (right-left)//2
            if self.check(piles, mid) > h:
                left = mid+1
            else:
                right = mid-1
                best = mid
        
        return best