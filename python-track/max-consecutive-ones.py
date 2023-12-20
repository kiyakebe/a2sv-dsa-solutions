class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter = 0
        max_num = 0
        for i in nums:
            if(i == 1): counter+=1
            elif(counter != 0):
                max_num = max(max_num, counter)
                counter=0
        max_num = max(max_num, counter)
        return max_num