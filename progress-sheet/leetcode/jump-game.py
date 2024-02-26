class Solution:
    def canJump(self, nums: List[int]) -> bool:
        moves = nums[0]

        for i in range(1, len(nums)):
            if moves <= 0:
                return False
            moves -= 1
            moves = max(moves, nums[i])
        
        return True
            