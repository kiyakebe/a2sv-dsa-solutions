class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        val = tickets[k]
        time = 0
        n = len(tickets)
        for i in range(n):
            if i <= k:
                if tickets[i] < val:
                    time += tickets[i]
                else:
                    time += val
            else:
                if tickets[i] < val:
                    time += tickets[i]
                else:
                    time += (val - 1)
        return time