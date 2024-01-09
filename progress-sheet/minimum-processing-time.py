class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort(reverse = True)
        tasks.sort()

        # we are going to take the max time of optimal time of each procesors
        min_time = float("-inf")
        for i in range(len(processorTime)):
            min_time = max(min_time, processorTime[i] + tasks[3 + i*4])
        
        return min_time