class RecentCounter:

    def __init__(self):
        self.q = deque()
        self.num = 0

    def ping(self, t: int) -> int:
        self.num += 1
        self.q.append(t)
        while self.q[0] < t - 3000:
            self.q.popleft()
            self.num -= 1

        return self.num


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)