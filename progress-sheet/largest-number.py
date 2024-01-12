class Solution:
    def compare(self, n1, n2):
            if n1 + n2 > n2 + n1:
                return -1
            return 1

    def largestNumber(self, nums: List[int]) -> str:
        nums_s = [str(x) for x in nums]

        nums_s = sorted(nums_s, key=cmp_to_key(self.compare))
        
        if nums_s[0] == "0":
            return "0"
        return "".join(nums_s)