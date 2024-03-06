class Solution:
    def hIndex(self, citations: List[int]) -> int:
        left = 0
        right = len(citations) - 1
        n = len(citations)
        h_index = float("-inf")
        
        while left <= right:
            mid = left + (right-left)//2

            if citations[mid] < n-mid:
                h_index = max(h_index, citations[mid])
                left = mid+1
            else:
                h_index = max(h_index, n-mid)
                right = mid-1

        return h_index