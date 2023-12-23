class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        st = set(list2)
        d = {}
        found_first_com = False
        min_sum = 0
        
        for i in range(len(list1)):
            if list1[i] in st:
                val = list2.index(list1[i]) + i
                if(not found_first_com):
                    min_sum = val
                    found_first_com = True
                min_sum = min(min_sum, val)
                if val not in d:
                    d[val] = []
                d[val].append(list1[i])

        print(d)
        return d[min_sum]
