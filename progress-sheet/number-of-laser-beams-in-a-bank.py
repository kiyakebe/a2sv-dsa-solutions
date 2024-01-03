class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        laser_count = 0
        device_count = [ i.count('1') for i in bank if i.count('1') > 0]
        for i in range(1, len(device_count)):
            laser_count += device_count[i-1] * device_count[i]
        return laser_count
