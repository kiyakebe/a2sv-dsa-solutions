class TimeMap:

    def __init__(self):
        self.time_map = defaultdict(list)        
        self.count = 0

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append([timestamp, value])
        self.count += 1

    def get(self, key: str, timestamp: int) -> str:
        if not self.time_map[key]:
            return ""
            
        index = bisect_left(self.time_map[key], [timestamp])
        if index == 0:
            if self.time_map[key][index][0] > timestamp:
                return ""
            else:
                return self.time_map[key][index][1]

        if index == len(self.time_map[key]):
            return self.time_map[key][index-1][1]
        
        if self.time_map[key][index][0] == timestamp:
            return self.time_map[key][index][1]

        return self.time_map[key][index-1][1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)