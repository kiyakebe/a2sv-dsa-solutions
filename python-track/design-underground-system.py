class UndergroundSystem:

    def __init__(self):
        self.checkin_record = defaultdict(tuple)
        self.station_record = defaultdict(list)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkin_record[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        s_station, s_time = self.checkin_record[id]
        total = t - s_time
        self.station_record[(s_station, stationName)].append(total)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return sum(self.station_record[(startStation, endStation)])/len(self.station_record[(startStation, endStation)])


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)