class Solution:
    def distanceBetweenBusStops(self, word2: List[int], start: int, destination: int) -> int:
        total_distance = 0
        dis_std_clockwise = 0

        for i in word2:
            total_distance += i 

        if(start < destination):
            for i in range(start, destination):
                dis_std_clockwise += word2[i]
        else:
            for i in range(destination, start):
                dis_std_clockwise += word2[i]

        return min(dis_std_clockwise, total_distance-dis_std_clockwise)
        