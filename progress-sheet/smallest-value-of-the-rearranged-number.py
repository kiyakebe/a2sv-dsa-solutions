class Solution:
    def smallestNumber(self, num: int) -> int:
        val = 0
        if num < 0:
            ls = list(str(num)[1:])
            ls.sort(reverse=True)
            print(ls)
            val = -1 * int(''.join(ls))
        else:
            ls = list(str(num))
            ls.sort()
            count = 0
            first = ''
            for i in range(len(ls)):
                if ls[i] != '0':
                    first = ls[i]
                    break
                count += 1
            val = int(''.join([first] + ['0']*count + ls[count+1:]))

        return val