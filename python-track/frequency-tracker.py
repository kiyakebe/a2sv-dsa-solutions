from collections import defaultdict
class FrequencyTracker:

    def __init__(self):
        self.d_val_freq = defaultdict(int)
        self.d_freq_count = defaultdict(int)

    def add(self, number: int) -> None:
        self.d_freq_count[self.d_val_freq[number]] -= 1
        self.d_val_freq[number] += 1
        self.d_freq_count[self.d_val_freq[number]] += 1

    def deleteOne(self, number: int) -> None:
        if self.d_val_freq[number] > 0:
            self.d_freq_count[self.d_val_freq[number]] -= 1
            self.d_val_freq[number] -= 1
            self.d_freq_count[self.d_val_freq[number]] += 1

    def hasFrequency(self, frequency: int) -> bool:
        if self.d_freq_count[frequency] > 0: return True
        return False


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)