# Problem: Find Players With Zero or One Losses - https://leetcode.com/problems/find-players-with-zero-or-one-losses

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        ans = [[],[]]
        loss_cnt = defaultdict(int)

        for match in matches:
            if match[0] not in loss_cnt:
                loss_cnt[match[0]] = 0
            
            loss_cnt[match[1]] += 1
        
        for k, v in loss_cnt.items():
            if v == 0:
                ans[0].append(k)
            elif v == 1:
                ans[1].append(k)

        ans[0].sort()
        ans[1].sort()

        return ans