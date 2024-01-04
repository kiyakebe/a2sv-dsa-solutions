class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        num1 = float("inf")
        num2 = float("inf")
        for i in nums:
            if num1 < i:
                return True
            elif num2 >= i:
                num2 = i
            else:
                num1 = i
        return False
