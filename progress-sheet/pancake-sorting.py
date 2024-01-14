class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        l = 0
        r = len(arr) - 1
        ans = []
        print(arr)
        while r > 0:
            _max = 0
            l = 0
            for i in range(r+1):
                if arr[i] > _max: 
                    _max = arr[i]
                    l = i

            if l != r:
                # take it to index 0
                arr = arr[l::-1] + arr[l+1:]
                ans.append(l+1)

                # take it to the right position
                arr = arr[r::-1] + arr[r+1:]
                ans.append(r+1)
            r -= 1
        return ans
