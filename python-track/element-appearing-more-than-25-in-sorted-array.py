class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        ans = arr[0]
        freq = n//4 + 1; counter=0
        for i in range(n):
            if ans == arr[i]: counter += 1
            else:
                ans = arr[i]
                counter = 1
            if(counter >= freq):
                break

        return ans

