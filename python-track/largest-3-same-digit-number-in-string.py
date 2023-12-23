class Solution:
    def largestGoodInteger(self, num: str) -> str:
        n = len(num)
        counter = 1
        good_int = []
        for i in range(1, n):
            if(num[i-1] == num[i]):
                counter += 1
            else:
                counter = 1
            if(counter == 3):
                good_int.append(num[i-2:i+1])
                counter = 1
        if(len(good_int) == 0): return ""

        good_int.sort() 
        return(good_int[-1])