class OrderedStream:
    # global orders
    def __init__(self, n: int):
        self.orders = [0 for x in range(n)]
        self.index = 0
        self.n = n

    def insert(self, idKey: int, value: str) -> List[str]:
        temp = []
        self.orders[idKey-1] = value
        while self.index < self.n and self.orders[self.index] != 0:
            temp.append(self.orders[self.index])
            self.index += 1
        return temp


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)