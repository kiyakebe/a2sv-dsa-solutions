# Problem: Minimum Time Difference - https://leetcode.com/problems/minimum-time-difference/

class Solution:
    def findMinDifference(self, time: List[str]) -> int:
        for i in range(len(time)):
            time[i]=time[i].split(':')
            time[i]=[int(time[i][0]),int(time[i][1])]

        mini=float('inf')
        time.sort()
        for i in range(1,len(time)):
            mini=min(mini,(time[i][0]-time[i-1][0])*60 +(time[i][1]-time[i-1][1]))
        mini=min(mini,(time[0][0]+23-time[-1][0])*60 +(time[0][1]+60-time[-1][1]))
        return mini
		