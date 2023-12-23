class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)
        pivot = 0
        for i in range(n-1):
            if(arr[i] == arr[i+1]): return False
            elif(arr[i] > arr[i+1]):
                pivot = i
                break
        if(pivot == 0): return False
        for i in range(pivot, n-1):
            if(arr[i] <= arr[i+1]):
                return False
        return True
