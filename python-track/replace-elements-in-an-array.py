class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        d= {i: 0 for i in nums}
        look_up = {}

        for i in operations:
            if i[0] not in look_up:
                d[i[0]] = i[1]
                look_up[i[1]] = i[0]
            else:
                d[look_up[i[0]]] = i[1]
                look_up[i[1]] = look_up[i[0]]
                del look_up[i[0]]

        for i in range(len(nums)):
            if d[nums[i]] != 0:
                nums[i] = d[nums[i]]
        
        return nums

