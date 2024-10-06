# Problem: Find Players With Zero or One Losses - https://leetcode.com/problems/find-players-with-zero-or-one-losses

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        loser = {}
        for i in matches:
            if i[1] not in loser:
                loser[i[1]] = 0
            loser[i[1]] += 1
        winner = {x[0] for x in matches if x[0] not in loser}

        loser_only_once = {x for x in loser if loser[x] == 1}
        return [sorted(list(winner)), sorted(list(loser_only_once))]