class Solution:
    def average(self, salary: List[int]) -> float:
        total = 0
        for i in salary:
            total += i
        min_s = min(salary)
        max_s = max(salary)
        
        total = total-min_s-max_s

        return total/(len(salary)-2)