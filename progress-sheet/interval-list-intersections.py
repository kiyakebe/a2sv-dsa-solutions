class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        ptr_f = 0
        ptr_s = 0
        ans = []
        while ptr_f < len(firstList) and ptr_s < len(secondList):
            temp = []

            if firstList[ptr_f][0] <= secondList[ptr_s][0]:
                temp.append(secondList[ptr_s][0])

                if firstList[ptr_f][1] >= secondList[ptr_s][0]:
                    if firstList[ptr_f][1] <= secondList[ptr_s][1]:
                        temp.append(firstList[ptr_f][1])
                        ptr_f += 1
                    else:
                        temp.append(secondList[ptr_s][1])
                        ptr_s += 1
                else:
                    ptr_f += 1
            else:
                temp.append(firstList[ptr_f][0])

                if firstList[ptr_f][0] <= secondList[ptr_s][1]:
                    if firstList[ptr_f][1] <= secondList[ptr_s][1]:
                        temp.append(firstList[ptr_f][1])
                        ptr_f += 1
                    else:
                        temp.append(secondList[ptr_s][1])
                        ptr_s += 1
                else:
                    ptr_s += 1
            if len(temp) > 1:
                ans.append(temp)

        return ans
            