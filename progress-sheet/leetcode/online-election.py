class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.times = times
        point_counter = defaultdict(int)
        max_vote = 0
        max_vited = 0

        n = len(persons)
        self.winner = [0]*n

        for i in range(n):
            point_counter[persons[i]] += 1
            if point_counter[persons[i]] >= max_vote:
                max_voted = persons[i]
                max_vote = point_counter[persons[i]]
            self.winner[i] = max_voted

    def q(self, t: int) -> int:
        winner_index = bisect_right(self.times, t)
        n = len(self.times)

        if winner_index < n and self.times[winner_index] == t:
            return self.winner[winner_index]
        return self.winner[winner_index-1]


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)

'''
check for one candidate
'''