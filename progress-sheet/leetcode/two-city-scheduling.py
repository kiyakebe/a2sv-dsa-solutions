class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:

        n = len(costs)
        for i in costs:
            i.append(i[0]-i[1])

        costs.sort(key = lambda x : x[-1])
        cost = 0
        for i in range(n//2):
            cost += costs[i][0]
        
        for i in range(n//2, n):
            cost += costs[i][1]
        
        return cost
       