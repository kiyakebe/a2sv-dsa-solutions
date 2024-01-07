class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        n = len(flips)
        string_ls = [0 for x in range(n)]
        index = 0
        count = 0
        max_insertion = 0

        for i in range(n):
            zero_indexed = flips[i]-1
            string_ls[zero_indexed] = 1
            max_insertion = max(max_insertion,zero_indexed)
            while index < n and string_ls[index] != 0:
                index += 1
                
            # -1 to balance the last increment 
            if index-1 == max_insertion:
                count += 1
            print(max_insertion, " ", index)
            
        return count
