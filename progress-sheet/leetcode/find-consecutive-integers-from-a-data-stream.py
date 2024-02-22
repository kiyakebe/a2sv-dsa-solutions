class DataStream:

    def __init__(self, value: int, k: int):
        self.v, self.k = value, k
        self.c = 0

    def consec(self, num: int) -> bool:
        if num == self.v:
            self.c += 1
            if self.c >= self.k:
                return True
        else:
            self.c = 0
            return False


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)